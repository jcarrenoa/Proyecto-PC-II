import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QCheckBox, QLineEdit, QMessageBox
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.uic import loadUi
import os

class example_ui(QMainWindow):
    def __init__(self):
        super().__init__()
        current_directory = os.path.dirname(os.path.abspath(__file__))
        loadUi(fr'{current_directory}/main.ui', self)
        self.show()