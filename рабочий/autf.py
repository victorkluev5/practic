from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QPushButton, QGridLayout, QLabel, QDialog, QMessageBox 
import sys 
from wind import Wind



class Autificator(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        widget = QWidget()    
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.login = QLabel("login")
        self.login_edit = QLineEdit()
        self.password = QLabel("password")
        self.password_edit = QLineEdit()
        self.btn_auth = QPushButton("Auth")
        self.btn_exit = QPushButton("Exit")       
        
        layout.addWidget(self.login)
        layout.addWidget(self.login_edit)
        layout.addWidget(self.password)
        layout.addWidget(self.password_edit)
        layout.addWidget(self.btn_auth)
        layout.addWidget(self.btn_exit)

        self.btn_auth.clicked.connect(self.btn_auth_click)
        self.btn_exit.clicked.connect(self.btn_exit_click)


    def btn_auth_click(self):
         self.wind = Wind()
         self.wind.show()
    
    def btn_exit_click(self):
        app.exit()
        

app = QApplication(sys.argv)
exe = Autificator()
exe.show()
app.exec()