import sys
from PySide6.QtWidgets import (QMainWindow, QWidget, QLayout, QApplication, 
                               QLabel)
app = QApplication(sys.argv)
from home import HomePage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PLOTLY")
        self.setMinimumSize(500, 500)
        self.page_handler()
    
    def page_handler(self):
        self.central_layout = HomePage
        self.setCentralWidget(self.central_layout)


if __name__ == "__main__":
    window = MainWindow()
    window.show()
    app.exec()
