from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel

class Wind(QMainWindow):
    def __init__ (self):
        super().__init__()

        self.setWindowTitle("Угадай кузов")
        self.setFixedSize(1000, 1000)

        layout = QVBoxLayout()
        lbl = QLabel()

        layout.addWidget(lbl)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)