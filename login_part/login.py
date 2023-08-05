# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(692, 503)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 311, 501))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-bottom-left-radius:30px;\n"
"border-top-left-radius:30px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 0, 381, 501))
        self.label_2.setStyleSheet("background-image: url(:/img/background.jpg);\n"
"border-top-right-radius:30px;\n"
"border-bottom-right-radius:30px")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 90, 121, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 210, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border: none;\n"
"font: 75 9pt \"Times New Roman\";\n"
"border-bottom:2px solid rgba(0,0,0,100);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 290, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border: none;\n"
"font: 9pt \"Times New Roman\";\n"
"border-bottom:2px solid rgba(0,0,0,100);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 370, 111, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(85, 170, 127);\n"
"border:none;\n"
"color:rgb(255,255,255);\n"
"border-radius:3px;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 220, 61, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border:none")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 300, 61, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(511, 10, 141, 41))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.minimize_button = QtWidgets.QPushButton(self.frame)
        self.minimize_button.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}\n"
"QPushButton:hover{\n"
"padding-bottom:5px;\n"
"}\n"
"\n"
"")
        self.minimize_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimize_button.setIcon(icon)
        self.minimize_button.setObjectName("minimize_button")
        self.minimize_button.clicked.connect(self.showMinimized)
        self.horizontalLayout.addWidget(self.minimize_button)
        self.close_button = QtWidgets.QPushButton(self.frame)
        self.close_button.clicked.connect(self.close)

        self.close_button.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}\n"
"QPushButton:hover{\n"
"padding-bottom:5px;\n"
"}\n"
"\n"
"")
        self.close_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_button.setIcon(icon1)
        self.close_button.setObjectName("close_button")
        self.horizontalLayout.addWidget(self.close_button)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 160, 81, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border:none")
        self.label_6.setObjectName("label_6")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(100, 160, 213, 39))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.teacher = QtWidgets.QRadioButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.teacher.setFont(font)
        self.teacher.setObjectName("teacher")
        self.horizontalLayout_2.addWidget(self.teacher)
        self.student = QtWidgets.QRadioButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.student.setFont(font)
        self.student.setObjectName("student")
        self.horizontalLayout_2.addWidget(self.student)
        self.student_2 = QtWidgets.QRadioButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.student_2.setFont(font)
        self.student_2.setObjectName("student_2")
        self.horizontalLayout_2.addWidget(self.student_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "用户登录"))
        self.pushButton.setText(_translate("MainWindow", "登录"))
        self.label_4.setText(_translate("MainWindow", "账号："))
        self.label_5.setText(_translate("MainWindow", "密码："))
        self.label_6.setText(_translate("MainWindow", "用户类型："))
        self.teacher.setText(_translate("MainWindow", "教师"))
        self.student.setText(_translate("MainWindow", "学生"))
        self.student_2.setText(_translate("MainWindow", "管理员"))
import img_rc
