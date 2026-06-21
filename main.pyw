


from PyQt5 import QtCore, QtGui, QtWidgets
from cryptography.fernet import Fernet
import base64
import hashlib
from tkinter import messagebox

sec_file = "secret_text.txt"

class Ui_MainWindow(object):

    def decrypt(self):
        password = self.lineEdit.text()

        if len(password) < 8:
            messagebox.showerror("ERROR", "Password must have atleast eight letters")
            exit()
            
        else:

            with open(sec_file, 'rb') as file:
                encrypted= file.read()

            
            self.key = base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest()[0:32])
            self.fernet = Fernet(self.key) 

            try:
                decrypted = self.fernet.decrypt(encrypted)
            except:
                messagebox.showerror("ERROR", "WRONG PASSWORD")
                exit()

            else:
                self.lineEdit.setText("")
                self.tabWidget.setTabVisible(1, True)
                self.tabWidget.setTabVisible(0,False)
                self.plainTextEdit.setPlainText(decrypted.decode())
                self.tabWidget.setCurrentIndex(1)


    def save_changes(self):
  
        encrypted = self.fernet.encrypt(self.plainTextEdit.toPlainText().encode())

        with open(sec_file, 'wb') as file:
            file.write(encrypted)

        quit()



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 821, 611))
        font = QtGui.QFont()
        font.setKerning(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setEnabled(True)
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(250, 0, 281, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(310, 380, 271, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(170, 380, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 440, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"border-radius : 15px;\n"
"color: white;\n"
"background-color: rgb(34, 225, 88)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-radius : 15px;\n"
"border : 3px solid rgb(34, 225, 88);\n"
"color : rgb(34, 225, 88);\n"
"background-color: white;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.decrypt)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit.setFont(QtGui.QFont('Arial', 15))
        self.plainTextEdit.setGeometry(QtCore.QRect(13, 96, 761, 451))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.clicked.connect(self.save_changes)
        self.pushButton.setGeometry(QtCore.QRect(310, 20, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setKerning(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"border-radius : 15px;\n"
"color: white;\n"
"background-color: rgb(245, 36, 75)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-radius : 15px;\n"
"border : 3px solid rgb(255, 17, 40);\n"
"color : rgb(255, 17, 40);\n"
"background-color: white;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab_2, "")
        self.tabWidget.setTabVisible(1, False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionEdit = QtWidgets.QAction(MainWindow)
        self.actionEdit.setObjectName("actionEdit")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Manager"))
        self.label.setText(_translate("MainWindow", "PASSWORD MANAGER"))
        self.label_2.setText(_translate("MainWindow", "Enter password:"))
        self.pushButton_2.setText(_translate("MainWindow", "OPEN"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Open"))
        self.pushButton.setText(_translate("MainWindow", "Save changes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Edit"))
        self.actionEdit.setText(_translate("MainWindow", "Edit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
