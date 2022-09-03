import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import sqlite3


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("interface/login.ui", self)
        self.loginbutton.clicked.connect(self.login_function)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createsignupactbutton.clicked.connect(self.gotocreate)

    def login_function(self):
        email = self.email.text()
        password = self.password.text()
        print("sucessfull loged in email: ", email, "and password:", password)

        '''verify if blank'''
        if len(email)==0 or len(password)==0:
            self.error.setText("Please input all fields \n"
                               " or create account")
        else:
            conn = sqlite3.connect("database/client.db")
            cur = conn.cursor()
            query = 'SELECT password FROM login_info WHERE email =\''+email+"\'"
            cur.execute(query)
            result_pass = cur.fetchone()[0]
            if result_pass == password:
                print("Sussesfull logged")
                self.error.setText("")
            else:
                self.error.setText("Invalid email or password")

    def gotocreate(self):
        createac = CreateAct()
        widget.addWidget(createac)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class CreateAct(QDialog):
    def __init__(self):
        super(CreateAct, self).__init__()
        loadUi("interface/createact.ui",self)
        self.signupbutton.clicked.connect(self.createactfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)

    def createactfunction(self):
        email = self.email.text()
        if self.password.text() == self.confirmpass.text():
            password = self.password.text()
            print("Successfuly create act with email", email, "and password: ", password)
            login = Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)


app = QApplication(sys.argv)
mainWindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainWindow)
widget.setFixedWidth(400)
widget.setFixedHeight(500)
widget.show()
app.exec_()
