import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QDockWidget, QListWidget, QWidget, 
    QVBoxLayout, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QGraphicsTextItem, QMenu, QGraphicsEllipseItem
)
from PyQt6.QtGui import QBrush, QColor, QPen, QPainter, QAction
from PyQt6.QtCore import Qt, QPointF, QRectF

class BlockItem(QGraphicsRectItem):
    def __init__(self, scene, block_type, title, x, y, width=120, height=80):
        super().__init__(x, y, width, height)
        self.scene = scene  # Pasar la escena como argumento y asignarla a self.scene
        self.block_type = block_type
        self.setPen(QPen(Qt.GlobalColor.black))
        self.setBrush(QBrush(QColor("#333333")))

        # Draw header
        self.header_height = 20
        self.header_rect = QRectF(x, y, width, self.header_height)
        self.header_brush = QBrush(self.get_header_color(block_type))

        # Title
        self.title_text = QGraphicsTextItem(title, self)
        self.title_text.setDefaultTextColor(Qt.GlobalColor.white)
        self.title_text.setPos(x + 5, y + 2)

        # Points of connection
        self.connection_points = {
            'condition': QPointF(x + 10, y + self.header_height + 10),
            'true': QPointF(x + width - 10, y + self.header_height + 5),
            'false': QPointF(x + width - 10, y + self.header_height + 25)
        }

        # Draw connection points and labels
        self.add_connection_point('condition', "condition")
        self.add_connection_point('true', "true")
        self.add_connection_point('false', "false")

    def get_header_color(self, block_type):
        colors = {
            "If": "#FF4500",          # OrangeRed
            "On_Start": "#FF6347",     # Tomato
            "On_Update": "#4682B4",    # SteelBlue
            "cycle": "#32CD32",        # LimeGreen
            "set_var": "#FFD700",      # Gold
            "set_arr": "#DAA520",      # GoldenRod
            "call_var": "#BA55D3",     # MediumOrchid
            "log": "#FF4500",          # OrangeRed
            "branch": "#2E8B57",       # SeaGreen
            "compare": "#8A2BE2",      # BlueViolet
            "for_iter": "#20B2AA",     # LightSeaGreen
            "add": "#00CED1",          # DarkTurquoise
            "sub": "#FF69B4",          # HotPink
            "mult": "#1E90FF",         # DodgerBlue
            "div": "#D2691E",          # Chocolate
            "div_int": "#FFB6C1",      # LightPink
            "mod": "#4B0082",          # Indigo
            "append_arr": "#7B68EE"    # MediumSlateBlue

        }
        return QColor(colors.get(block_type, "#FF4500")) 

    def add_connection_point(self, point_name, label):
        point = self.connection_points[point_name]
        circle = QGraphicsEllipseItem(point.x() - 3, point.y() - 3, 6, 6, self)
        circle.setPen(QPen(Qt.GlobalColor.black))
        circle.setBrush(QBrush(Qt.GlobalColor.blue))
        self.scene.addItem(circle)
        
        text = QGraphicsTextItem(label, self)
        text.setDefaultTextColor(Qt.GlobalColor.white)
        text.setPos(point.x() + 5, point.y() - 8)
        self.scene.addItem(text)
    
    def paint(self, painter, option, widget):
        # Draw the main rectangle
        super().paint(painter, option, widget)
        # Draw the header
        painter.setBrush(self.header_brush)
        painter.drawRect(self.header_rect)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configurar la ventana principal
        self.setWindowTitle("Visual Scripting")
        self.setGeometry(100, 100, 1200, 800)

        # Crear el área central
        self.graphics_view = QGraphicsView(self)
        self.graphics_scene = QGraphicsScene(self)
        self.graphics_view.setScene(self.graphics_scene)
        self.setCentralWidget(self.graphics_view)

        # Cambiar el color de fondo del área de trabajo a gris
        self.graphics_view.setBackgroundBrush(QBrush(QColor("#808080")))

        # Habilitar el menú contextual personalizado en el área de trabajo
        self.graphics_view.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.graphics_view.customContextMenuRequested.connect(self.show_context_menu)

        # Panel lateral izquierdo para scripts
        self.create_script_panel()

        # Panel lateral derecho para settings y variables
        self.create_settings_panel()

    def create_script_panel(self):
        dock = QDockWidget("Scripts", self)
        dock.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea)
        script_list = QListWidget(dock)
        script_list.addItem("bubble sort")
        dock.setWidget(script_list)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, dock)

    def create_settings_panel(self):
        dock = QDockWidget("Settings and Variables", self)
        dock.setAllowedAreas(Qt.DockWidgetArea.RightDockWidgetArea)
        settings_widget = QWidget(dock)
        settings_layout = QVBoxLayout(settings_widget)

        # Algorithm settings
        settings_layout.addWidget(QListWidget())
        
        dock.setWidget(settings_widget)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock)

    def show_context_menu(self, pos):
        context_menu = QMenu(self)

        # Lista de bloques a añadir
        block_types = ["If", "On_Start", "On_Update", "cycle", "set_var", "set_arr", "call_var", "log", "branch", "compare", "for_iter", "add", "sub", "mult", "div", "div_int", "mod", "append_arr"]

        # Crear acciones para cada bloque
        for block_type in block_types:
            action = QAction(block_type, self)
            action.triggered.connect(lambda checked, bt=block_type: self.add_block(bt, pos))
            context_menu.addAction(action)

        context_menu.exec(self.graphics_view.mapToGlobal(pos))

    def add_block(self, block_type, pos):
        # Convertir la posición del clic a coordenadas de la escena
        scene_pos = self.graphics_view.mapToScene(pos)
        block = BlockItem(self.graphics_scene, block_type, block_type, scene_pos.x(), scene_pos.y())  # Pasar self.graphics_scene como argumento
        self.graphics_scene.addItem(block)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
