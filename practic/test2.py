import sys 
from  PyQt6.QtWidgets import QWidget,  QApplication, QMainWindow, QLabel, QHBoxLayout, QLineEdit, QComboBox, QPushButton, QVBoxLayout, QGridLayout, QDialog, QMessageBox
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont, QPixmap
# from test import captc, pattern
from wind import Wind

class Avtoriz(QMainWindow):
    
    # def enterClicked(self, login, password):
    #         if login =="1" and password =="1":
    #             self.avtoriz = Avtoriz2()
    #             self.avtoriz.show()
    #         else:
    #             self.counter += 1
    #             self.modal = CaptchaDialog(count=self.counter)
    #             self.modal.show()
    
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Авторизация ")
        self.setFixedSize(300,300)
        
        self.number_class = QComboBox()
        
        
        self.lbl_0 = QLabel("Логин:")
        self.login_lbl = QLineEdit()
        self.lbl_1 = QLabel("Пароль:")
        self.password_lbl = QLineEdit()
        self.btn_add = QPushButton("Вход")
        self.btn_exit = QPushButton("Выход")
        
        
        layout = QGridLayout()
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        
        layout.addWidget(self.lbl_0)
        layout.addWidget(self.login_lbl)
        layout.addWidget(self.lbl_1)
        layout.addWidget(self.password_lbl)
        layout.addWidget(self.btn_add)
        layout.addWidget(self.btn_exit)
        
        self.btn_add.clicked.connect(self.btn_add_click)
        
        # self.btn_add.clicked.connect(lambda:self.enterClicked(self.login_lbl.text(), self.password_lbl.text()))
        self.btn_exit.clicked.connect(self.btn_exit_click)
        
        
    def btn_add_click(self):
        username = self.login_lbl.text()
        password = self.password_lbl.text()

        if username == "1" and password == "1":
            
            self.avtoriz = Wind()
            self.avtoriz.show()
        else:
            # self.captcha_dialog = QTimer()
            # self.captcha_dialog.start_timer()
            self.captcha = CaptchaDialog()
            self.captcha.show()

        # if self.captcha_dialog.exec() == QDialog.DialogCode.Accepted:
        #     QMessageBox.information(self, "Успех", "Вход выполнен после капчи")

        # else:
        #     QMessageBox.warning(self, "Ошибка", "Неверные данные и капча")
        #     self.login_attempts = 0
        

    # def btn_add_click(self):
    #     self.avtoriz = Avtoriz2()
    #     self.avtoriz.show()

        
    def btn_exit_click(self):
        app.exit()

class CaptchaDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Капча")
        self.label = QLabel("Введите капчу:")
        self.captha= QLabel()
        self.captha.setPixmap(QPixmap("capctha.jpg"))
        self.textbox = QLineEdit()
        self.button = QPushButton("Проверить")
        self.button.clicked.connect(self.verify_captcha)

        self.timer_label = QLabel("Таймер: 10")
        self.timer_counter = 10
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_timer)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.textbox)
        layout.addWidget(self.timer_label)
        layout.addWidget(self.button)
        layout.addWidget(self.captha)

        self.setLayout(layout)
        

    def verify_captcha(self):
        captcha = self.textbox.text()
    # Здесь вы можете добавить свою логику проверки капчи
        print("Проверка капчи:", captcha)


        if captcha.lower() ==  "irf6h4" : # Замените это условие на свою проверку капчи
            self.accept()
        else:
            self.textbox.setDisabled(True) # Блокировка поля ввода
            self.timer_counter = 10
            self.timer.start()
            QMessageBox.critical(self, "Ошибка", "Неправильная капча")

    def start_timer(self):
        self.timer_counter = 10
        self.timer.start()

    def update_timer(self):
        self.timer_counter -= 1
        self.timer_label.setText(f"Таймер: {self.timer_counter}")

        if  self.timer_counter == 0:
            self.timer.stop()
            self.textbox.setDisabled(False)


app = QApplication(sys.argv)
exe = Avtoriz()
exe.show()
app.exec()