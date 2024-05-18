from App import MainWindow
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())


