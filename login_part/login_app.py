from login import Ui_MainWindow
from graphic_user_interface import MyWindow
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QMessageBox
from PyQt5 import QtGui
from app import check_teacher_password, check_student_password
import webbrowser
import sys


class LoginWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 初始化窗体
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.pushButton.clicked.connect(self.go_to_inter)
        self.inter_window = MyWindow()

    def go_to_inter(self):
        account = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if self.teacher.isChecked():
            self.teacher_account_check(account, password)
        elif self.student.isChecked():
            self.student_account_check(account,password)

    def teacher_account_check(self, account, password):
        res = check_teacher_password(account, password)
        if res == 1:
            self.close()
            webbrowser.open("http://127.0.0.1:5000", new=0, autoraise=True)
        elif res == 2:
            title = '错误提示'
            info = "查无此账号"
            QMessageBox.warning(self, title, info)
        elif res == 0:
            title = '错误提示'
            info = "密码错误，请确认密码或用户类型是否正确"
            QMessageBox.warning(self, title, info)

    def student_account_check(self, account, password):
        res = check_student_password(account, password)
        if res == 1:
            self.close()
            self.inter_window.show()
        elif res == 2:
            title = '错误提示'
            info = "查无此账号"
            QMessageBox.warning(self, title, info)
        elif res == 0:
            title = '错误提示'
            info = "密码错误，请确认密码或用户类型是否正确"
            QMessageBox.warning(self, title, info)

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



if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = LoginWindow()
    window.show()

    sys.exit(app.exec_())