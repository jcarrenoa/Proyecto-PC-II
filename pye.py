#EJEMPLOS 

import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QLabel, QWidget
from PyQt6.QtGui import QPainter, QColor, QBrush, QPen
from PyQt6.QtCore import Qt

class RectangleWithButtons:
    def __init__(self, parent):
        self.parent = parent

        # Crear dos botones simulados
        self.button1 = QPushButton('Botón 1', parent)
        self.button1.setGeometry(10, 10, 80, 30)

        self.button2 = QPushButton('Botón 2', parent)
        self.button2.setGeometry(10, 50, 80, 30)

        # Crear una etiqueta
        self.label = QLabel('Etiqueta', parent)
        self.label.setGeometry(200, 10, 150, 30)

    def paintEvent(self, event):
        painter = QPainter(self.parent)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing) # Para mejorar la calidad del dibujo

        # Dibujar el rectángulo
        rect = self.parent.rect()
        painter.setPen(QPen(Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine))
        painter.setBrush(QBrush(Qt.GlobalColor.blue, Qt.BrushStyle.SolidPattern))
        painter.drawRect(0, 0, 100, 100)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('Rectángulo con botones y etiqueta')
    window.setGeometry(100, 100, 400, 400)

    rectangle = RectangleWithButtons(window)
    # Llamar a la función paintEvent para dibujar el rectángulo
    rectangle.paintEvent(None)

    window.show()
    sys.exit(app.exec())