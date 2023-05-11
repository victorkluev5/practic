from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel

class Wind(QMainWindow):
    def __init__ (self):
        super().__init__()

        self.setWindowTitle("Угадай кузов")
        self.setFixedSize(500, 500)
        
        layout = QVBoxLayout()
        lbl = QLabel("Прошли вход")

        layout.addWidget(lbl)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)