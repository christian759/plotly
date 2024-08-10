from PySide6.QtWidgets import QWidget, QLayout, QLabel, QPushButton, QVBoxLayout

class Welcome_ui(QWidget):
    def __init__(self,):
        super().__init__()
        self.setMinimumSize(700, 800)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.close_button = QPushButton("close")
        self.close_button.clicked.connect(Welcome_ui.close)
        self.inner_widget(layout=self.layout)
        
    def inner_widget(self, layout):
        layout.addWidget(self.close_button)
        