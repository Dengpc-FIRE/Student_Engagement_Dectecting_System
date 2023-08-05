import json
import sys
import cv2
import os
import io
import torch
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageQt
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QMessageBox
from PyQt5.QtCore import QTimer, QThread
from PyQt5 import QtGui
from PyQt5.QtGui import QImage, QPixmap
from ui_design_littleversion import Ui_MainWindow
from load_model import get_model
from app import add_record, query_student, update_student_info, delete_student
from datetime import datetime
from statistics import mean

engagements = [0] * 300
percent = 0
sum_seconds = 0
times_of_engaged = 0
times_of_unengaged = 0


class MyWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)  # 初始化窗体
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.camera_timer = None
        self.learn_timer = None
        self.cap = cv2.VideoCapture(0)  # 摄像头
        self.face_detecting = False
        self.img_path = 'temp.jpg'
        self.model, self.data_transform = get_model()
        self.model.eval()
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.start_widget()
        json_path = 'class_indices.json'
        assert os.path.exists(json_path), "file: '{}' dose not exist.".format(json_path)
        with open(json_path, "r") as f:
            self.class_indict = json.load(f)
        self.studentname = 'Student1'
        self.studentid = "202111070201"
        # add_record(self.studentname, self.studentid, 0, 'undetermined', datetime.now())
        self.last_save_time = datetime.now()
        self.engaged_data = []
        self.unengaged_data = []

    # mouse拖动
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.isMaximized() == False:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, mouse_event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos() - self.m_Position)  # 更改窗口位置
            mouse_event.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    # maximize
    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
            self.pushButton_maxsize.setIcon(QtGui.QIcon("icons/maximize.png"))
        else:
            self.showMaximized()
            self.pushButton_maxsize.setIcon(QtGui.QIcon("icons/maximize.png"))

    def start_widget(self):
        # 初始化定时器， 定时读取摄像头拍摄的图片
        self.camera_timer = QTimer(self)
        self.learn_timer = QTimer(self)
        self.learn_timer.setInterval(1000)
        self.learn_timer.timeout.connect(self.update_time)
        # 页面切换
        self.pushButton_2.clicked.connect(self.show_data)
        # 打开摄像头
        self.pushButton_open.clicked.connect(self.open_camera)
        # 关闭摄像头
        self.pushButton_close_2.clicked.connect(self.close_camera)
        # 是否开启人脸检测
        self.pushButton.clicked.connect(self.change_face_detect_status)

        self.pushButton_maxsize.clicked.connect(self.restore_or_maximize_window)

    def show_data(self):
        if self.stackedWidget.currentIndex() == 0:
            self.stackedWidget.setCurrentIndex(1)
        else :
            self.stackedWidget.setCurrentIndex(0)

    def open_camera(self):
        if self.cap.isOpened():
            self.camera_timer.start(16)
            self.camera_timer.timeout.connect(self.show_image)
        else:
            QMessageBox.critical(self, 'Error', '摄像头未打开！！！')
            return None

    def show_image(self):
        flag, frame = self.cap.read()
        frame = cv2.resize(frame, (640, 480))
        frame = cv2.flip(frame, 1)  # 水平翻转

        if self.face_detecting:
            detect_res = self.face_detect(frame)
            if detect_res is not None:
                frame = detect_res
            # 在plt上绘制参与度变化曲线图
            plt.cla()
            plt.title('Engagement Changes')
            plt.plot(engagements)

        width, height = frame.shape[:2]
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # BGR转化为RGB通道

        # 将读取到的帧图像转化为QImage形式
        img = QImage(frame.data, height, width, QImage.Format_RGB888)
        self.label_3.setPixmap(QPixmap.fromImage(img))  # 在QLabel中显示图像

    def face_detect(self, img):
        face_cascade = cv2.CascadeClassifier('detector/lbpcascade_frontalface_improved.xml')  # 正脸检测
        profile_face_cascade = cv2.CascadeClassifier('detector/lbpcascade_profileface.xml')  # 侧脸检测"""

        frontal_faces = face_cascade.detectMultiScale(img, 1.3, 2)  # 正脸
        right_profile_faces = profile_face_cascade.detectMultiScale(img, 1.3, 2)  # 右侧脸
        reverse_img = cv2.flip(img, 1)
        left_profile_faces = profile_face_cascade.detectMultiScale(reverse_img, 1.3, 2)  # 左侧脸

        # engagement detecting
        face_input = Image.fromarray(np.uint8(img))
        face_input = self.data_transform(face_input)
        face_input = torch.unsqueeze(face_input, dim=0)


        # 做预测
        with torch.no_grad():
            output = torch.squeeze(self.model(face_input.to(self.device))).cpu()
            predict = torch.softmax(output, dim=0)
            predict_cla = torch.argmax(predict).numpy()
        student_status = self.class_indict[str(predict_cla)]
        possibility = float(predict[0].numpy() + predict[1].numpy())

        if student_status == 'unengaged':
            self.unengaged_data.append(possibility)
        else:
            self.engaged_data.append(possibility)

        if (len(self.engaged_data) + len(self.unengaged_data)) == 7:
            if len(self.engaged_data) > len(self.unengaged_data):
                if datetime.now().second != self.last_save_time.second:
                    update_student_info(studentname=self.studentname, status='engaged', engagement_score=mean(self.engaged_data),
                                        time=datetime.now())
                    self.last_save_time = datetime.now()
            else :
                if datetime.now().second != self.last_save_time.second:
                    update_student_info(studentname=self.studentname, status='unengaged', engagement_score=mean(self.unengaged_data),
                                        time=datetime.now())
                    self.last_save_time = datetime.now()
        self.engaged_data = []
        self.unengaged_data = []

        global times_of_unengaged, times_of_engaged
        if student_status == 'unengaged':
            times_of_unengaged += 1
        else:
            times_of_engaged += 1
        global engagements, percent

        percent = float(predict[0].numpy() + predict[1].numpy())
        engagements = engagements[1:] + [percent]
        if len(frontal_faces) != 0:  # 正脸标注
            for (x, y, w, h) in frontal_faces:
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        elif len(right_profile_faces) != 0:  # 右侧脸标注
            for (x, y, w, h) in right_profile_faces:
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        elif len(left_profile_faces) != 0:  # 左侧脸标注
            for (x, y, w, h) in left_profile_faces:
                img = cv2.rectangle(reverse_img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                img = cv2.flip(img, 1)
        color = (0, 0, 255) if student_status == 'unengaged' else (0, 255, 0)
        cv2.putText(img, f"{student_status} {possibility}", (10, 40), 2, 1.2, color, 2, cv2.LINE_AA)
        return img

    def close_camera(self):
        self.camera_timer.stop()
        # self.cap.release()
        self.label_3.clear()

    def update_time(self):
        global sum_seconds
        sum_seconds += 1

    def get_real_time(self, seconds):
        hour = seconds // 3600
        left = seconds - hour * 3600
        min = left // 60
        sec = left - min * 60
        if hour < 10:
            hour = '0' + str(hour)
        if min < 10:
            min = '0' + str(min)
        if sec < 10:
            sec = '0' + str(sec)
        return str(hour) + ':' + str(min) + ':' + str(sec)

    def change_face_detect_status(self):
        global sum_seconds
        if self.face_detecting:
            self.learn_timer.stop()
            self.lcdNumber.display(self.get_real_time(sum_seconds))
            pe = round(times_of_engaged/(times_of_engaged + times_of_unengaged) * 100, 2)
            poe = 100 - pe
            self.lcdNumber_2.setSmallDecimalPoint(True)
            self.lcdNumber_2.display(pe)
            self.lcdNumber_3.setSmallDecimalPoint(True)
            self.lcdNumber_3.display(poe)
            self.face_detecting = False
        elif not self.face_detecting:
            self.face_detecting = True
            self.learn_timer.start()


if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()

    sys.exit(app.exec_())