import sys
from PySide6.QtWidgets import (QMainWindow, QWidget, QLayout, QApplication, 
                               QLabel)
from welcome import Welcome_ui
from front import HomePage

intro: bool = False
user: str = "USER" 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PLOTLY")
        self.setMinimumSize(500, 500)
        self.central_layout = QWidget()
        self.setCentralWidget(self.central_layout)
        self.home_handler()
    
    def home_handler(self):
        if intro == False:
            self.central_layout = Welcome_ui()
        else:
            self.UI()
    
    def UI(self):
        home = HomePage(user)
        self.central_layout = home


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
