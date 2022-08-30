import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("login.ui", self)
        self.loginbutton.clicked.connect(self.login_function)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createsignupactbutton.clicked.connect(self.gotocreate)

    def login_function(self):
        email = self.email.text()
        password = self.password.text()
        print("sucessfull loged in email: ", email, "and password:", password)

    def gotocreate(self):
        createac = CreateAct()
        widget.addWidget(createac)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class CreateAct(QDialog):
    def __init__(self):
        super(CreateAct, self).__init__()
        loadUi("createact.ui",self)
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
