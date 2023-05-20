from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
class TestWindow(QMainWindow):
    spisoc = []
    def __init__(self):
        super().__init__()
        self.setFixedSize(500,200)

        self.name = QLabel("Введите свое Имя и Фамилию")
        self.edit = QLineEdit()
        self.course = QLabel("Введите Группу")
        self.edit1 = QLineEdit()
        box = QVBoxLayout()
        wid = QWidget()
        wid.setLayout(box)
        box.addWidget(self.name)
        box.addWidget(self.edit)
        box.addWidget(self.course)

        box.addWidget(self.edit1)

        lbl1 = QLabel("Какой тип автомобиля вы предпочитаете?")
        self.rb1 = QRadioButton(text="Седан")
        self.rb2 = QRadioButton(text="Хэтчбек")
        self.rb3 = QRadioButton(text="Внедорожник")
        self.rb4 = QRadioButton(text="Купе")
        vbox = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(vbox)
        vbox.addWidget(lbl1)
        vbox.addWidget(self.rb1)
        vbox.addWidget(self.rb2)
        vbox.addWidget(self.rb3)
        vbox.addWidget(self.rb4)

        lbl2 = QLabel("Какой бюджет у вас на автомобиль?")
        self.rb1_1 = QRadioButton(text="До 300 000 руб")
        self.rb2_1 = QRadioButton(text="300 000 руб - 700 000 руб")
        self.rb3_1 = QRadioButton(text="700 000 руб - 1 000 000 руб")
        self.rb4_1 = QRadioButton(text="Более 1 000 000 руб")
        vbox_2 = QVBoxLayout()
        widget2 = QWidget()
        widget2.setLayout(vbox_2)
        vbox_2.addWidget(lbl2)
        vbox_2.addWidget(self.rb1_1)
        vbox_2.addWidget(self.rb2_1)
        vbox_2.addWidget(self.rb3_1)
        vbox_2.addWidget(self.rb4_1)


        lbl3 = QLabel("Какие опции вам необходимы?")
        self.rb1_2 = QRadioButton(text="Кондиционер")
        self.rb2_2 = QRadioButton(text="Навигационная система")
        self.rb3_2 = QRadioButton(text="Камера заднего вида")
        self.rb4_2 = QRadioButton(text= "Круиз-контроль")
        vbox_3 = QVBoxLayout()
        widget3 = QWidget()
        widget3.setLayout(vbox_3)
        vbox_3.addWidget(lbl3)
        vbox_3.addWidget(self.rb1_2)
        vbox_3.addWidget(self.rb2_2)
        vbox_3.addWidget(self.rb3_2)
        vbox_3.addWidget(self.rb4_2)

        lbl7 = QLabel("Результаты теста:")
        self.v6 = QLabel(self.rb1_2.text())
        self.v2 = QLabel()
        self.v3 = QLabel()
        self.v4 = QLabel()
        self.v5 = QLabel()
        self.res = QLabel()
        vbox7 = QVBoxLayout()
        widget7 = QWidget()
        widget7.setLayout(vbox7)
        vbox7.addWidget(lbl7)
        vbox7.addWidget(self.v6)
        vbox7.addWidget(self.v2)
        vbox7.addWidget(self.v3)
        vbox7.addWidget(self.v4)
        vbox7.addWidget(self.v5)
        vbox7.addWidget(self.res)
        btn_save = QPushButton("Сохранить")
        btn_save.clicked.connect(self.save)
        vbox7.addWidget(btn_save)


        pagelayout = QVBoxLayout()
        self.button_layout = QHBoxLayout()
        self.stacklayout = QStackedLayout()

        pagelayout.addLayout(self.stacklayout)
        pagelayout.addLayout(self.button_layout)

        self.btnb = QPushButton("back")
        self.btn = QPushButton("next")

        self.btnb.clicked.connect(self.activate_tab_b)
        self.btn.clicked.connect(self.activate_tab_v)

        self.stacklayout.addWidget(wid)
        self.button_layout.addWidget(self.btnb)
        self.button_layout.addWidget(self.btn)

        self.stacklayout.addWidget(widget)

        self.stacklayout.addWidget(widget2)

        self.stacklayout.addWidget(widget3)

        # self.stacklayout.addWidget(widget6)

        self.stacklayout.addWidget(widget7)



        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)

        with open("style.css", "r") as css:
            self.setStyleSheet(css.read())

    def activate_tab_v(self):
        self.stacklayout.setCurrentIndex(self.stacklayout.currentIndex()+1)

        if self.rb1.isChecked():
            self.spisoc.append(self.rb1.text())

        if self.rb2.isChecked():
            self.spisoc.append(self.rb2.text())
        
        if self.rb3.isChecked():
            self.spisoc.append(self.rb3.text())

        if self.rb4.isChecked():
            self.spisoc.append(self.rb4.text())

        if self.rb1_1.isChecked():
            self.spisoc.append(self.rb1_1.text())

        if self.rb2_1.isChecked():
            self.spisoc.append(self.rb2_1.text())
        
        if self.rb3_1.isChecked():
            self.spisoc.append(self.rb3_1.text())

        if self.rb4_1.isChecked():
            self.spisoc.append(self.rb4_1.text())

        if self.rb1_2.isChecked():
            self.spisoc.append(self.rb1_2.text())

        if self.rb2_2.isChecked():
            self.spisoc.append(self.rb2_2.text())

        if self.rb3_2.isChecked():
            self.spisoc.append(self.rb3_2.text())

        if self.rb4_2.isChecked():
            self.spisoc.append(self.rb4_2.text())

    def activate_tab_b(self):
        self.stacklayout.setCurrentIndex(self.stacklayout.currentIndex()-1)

    def result(self):
        result = "Результаты:\n"
        for i in range(self.activate_tab_v):
            result += f"Вопрос {i+1}: {self.spisoc[i]['question']}\n"
            result += f"Ответ: {self.spisoc[i]}\n\n"
        QMessageBox.information(self, "Результаты", result)

        # self.setFixedSize(500, 300)
        # self.res.setText(f"Ваш результат:{self.e}")
    def save(self):
        info = f"Фамилия и Имя:{self.edit.text()} \n"
        cour = f"Группа:{self.edit1.text()} \n"
        txt = f"Ваш результат:{self.v6.text()} \n"
        txt1 = f"Ваш результат:{self.v2.text()} \n"
        txt2 = f"Ваш результат:{self.v3.text()} \n"
        txt5 = f"Ваш результат:{self.e} \n"

        with open("results.txt", "w", encoding="utf-8") as f:
            f.write(info)
            f.write(cour)
            f.write(txt)
            f.write(txt1)
            f.write(txt2)
            f.write(txt5)
