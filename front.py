from PySide6.QtWidgets import QWidget, QLabel, QBoxLayout

class HomePage(QWidget):
    def __init__(self, name):
        super().__init__()
        self.name =  name
        self.layout = QBoxLayout()
        self.setLayout(self.layout)
