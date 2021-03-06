# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    stylePopupError = ("background-color: rgb(85, 85, 255); border-radius: 15px")
    stylePopupOk = ("background-color: rgb(0, 255,0); border-radius: 15px")
    def checkField(self): #averiguando a guia te Tema
        TextTheme = ""

        def showMessage(message):
            self.popup_error.show()
            self.label_error.setText(message)

        if not self.type_theme.text():
            TextTheme = " Theme Empty "
        else:
            TextTheme = ""

        if TextTheme != '':
            text = TextTheme
            showMessage(text)
            self.popup_error.setStyleSheet(self.stylePopupError)
        else:
            text = " Theme Ok! "
            if self.my_business.isChecked():
                text = text + "MB Ok"
            showMessage(text)
            self.popup_error.setStyleSheet(self.stylePopupOk)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(757, 796)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/favicon/IAGO.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top = QtWidgets.QFrame(self.centralwidget)
        self.top.setMaximumSize(QtCore.QSize(16777215, 50))
        self.top.setStyleSheet("")
        self.top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top.setObjectName("top")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.top)
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.popup_error = QtWidgets.QFrame(self.top)
        self.popup_error.setMaximumSize(QtCore.QSize(200, 850))
        self.popup_error.setStyleSheet(self.stylePopupError)
        self.popup_error.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.popup_error.setFrameShadow(QtWidgets.QFrame.Raised)
        self.popup_error.setObjectName("popup_error")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.popup_error)
        self.horizontalLayout_3.setContentsMargins(10, 3, 10, 3)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_error = QtWidgets.QLabel(self.popup_error)
        self.label_error.setScaledContents(False)
        self.label_error.setObjectName("label_error")
        self.horizontalLayout_3.addWidget(self.label_error)
        self.close_popup = QtWidgets.QPushButton(self.popup_error)
        self.close_popup.setMinimumSize(QtCore.QSize(40, 30))
        self.close_popup.setMaximumSize(QtCore.QSize(30, 30))
        self.close_popup.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(60, 187, 255);\n"
"    color:rgb(255, 255, 255);\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 206, 28);\n"
"    color: rgb(0,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(20, 50, 300);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.close_popup.setObjectName("close_popup")
        self.horizontalLayout_3.addWidget(self.close_popup)
        self.horizontalLayout_2.addWidget(self.popup_error)
        self.verticalLayout.addWidget(self.top)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login = QtWidgets.QFrame(self.frame)
        self.login.setMinimumSize(QtCore.QSize(450, 450))
        self.login.setMaximumSize(QtCore.QSize(450, 450))
        self.login.setStyleSheet("background-color: rgb(157, 217, 255);\n"
"border-radius: 30px;")
        self.login.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.login.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login.setObjectName("login")
        self.logo = QtWidgets.QFrame(self.login)
        self.logo.setGeometry(QtCore.QRect(70, 70, 300, 161))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QtCore.QSize(300, 140))
        self.logo.setMaximumSize(QtCore.QSize(1000, 1000))
        self.logo.setStyleSheet("background-image: url(:/logo/IAGO.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"border-radius: 0px")
        self.logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo.setObjectName("logo")
        self.type_theme = QtWidgets.QLineEdit(self.login)
        self.type_theme.setGeometry(QtCore.QRect(70, 260, 300, 46))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.type_theme.setFont(font)
        self.type_theme.setStyleSheet("QLineEdit{\n"
"    border: 3px solid rgb(105, 175, 255);\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"    background-color: rgb(105, 132, 255);\n"
"    color: rgb(0,0,0);\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(255, 255, 255);\n"
"    background-color: rgb(206, 166, 23);\n"
"    color: rgb(255, 255, 255)\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(255, 243, 151);\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(255, 206, 28)\n"
"}")
        self.type_theme.setMaxLength(40)
        self.type_theme.setObjectName("type_theme")
        self.my_business = QtWidgets.QCheckBox(self.login)
        self.my_business.setGeometry(QtCore.QRect(80, 320, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.my_business.setFont(font)
        self.my_business.setStyleSheet("QCheckBox::indicator {\n"
"    border: 2px solid rgb(85, 85, 255);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 6px;\n"
"    background-color: rgb(255, 206, 28);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    border: 2px solid rgb(85, 85, 255);\n"
"    background-color: rgb(105, 132, 255);\n"
"}")
        self.my_business.setObjectName("my_business")
        self.button_do_it = QtWidgets.QPushButton(self.login)
        self.button_do_it.setGeometry(QtCore.QRect(150, 360, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setBold(True)
        font.setWeight(75)
        self.button_do_it.setFont(font)
        self.button_do_it.setStyleSheet("QPushButton {\n"
"    background-color: rgb(105, 175, 255);\n"
"    border-radius: 25px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(105, 132, 255);\n"
"    border: 5px solid rgb(255, 255, 255);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(157, 217, 255);\n"
"    border: 5px solid rgb(105, 132, 255);\n"
"    color: rgb(105, 132, 255);\n"
"}")
        self.button_do_it.setObjectName("button_do_it")
        self.horizontalLayout.addWidget(self.login)
        self.verticalLayout.addWidget(self.frame)
        self.bottom = QtWidgets.QFrame(self.centralwidget)
        self.bottom.setMaximumSize(QtCore.QSize(16777215, 30))
        self.bottom.setStyleSheet("background-color: rgb(105, 132, 255);")
        self.bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom.setObjectName("bottom")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.bottom)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.bottom)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.bottom)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 757, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.close_popup.clicked.connect(lambda: self.popup_error.hide()) #faz com que a janela de erro feche quando clicarmos em 'close'
        self.popup_error.hide() #faz com que o erro apare??a como oculto

        self.button_do_it.clicked.connect(self.checkField)
        self.button_do_it.clicked.connect(self.button_click)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def button_click(self):
        # shost is a QString object
        shost = self.type_theme.text()
        print (shost)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Input"))
        self.label_error.setText(_translate("MainWindow", "Erro"))
        self.close_popup.setText(_translate("MainWindow", "close"))
        self.type_theme.setPlaceholderText(_translate("MainWindow", "Type Your Theme"))
        self.my_business.setText(_translate("MainWindow", "My Business"))
        self.button_do_it.setText(_translate("MainWindow", "Do it"))
        self.label.setText(_translate("MainWindow", "Coprights: Efraim | ASTRO Com.   "))
import files_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
