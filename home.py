from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt

HomePage = QWidget()
Homelayout = QVBoxLayout()

welcome = QLabel("Welcome User")
welcome.setAlignment(Qt.AlignCenter)
Homelayout.addWidget(welcome)
HomePage.setLayout(Homelayout)