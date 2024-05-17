from App import WindowsMain
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = WindowsMain.example_ui()
    sys.exit(app.exec())