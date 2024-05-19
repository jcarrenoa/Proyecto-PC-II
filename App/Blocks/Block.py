import App.Blocks.blocksDesing as blocksDesing
from PyQt6.QtWidgets import QGraphicsRectItem, QGraphicsTextItem, QGraphicsEllipseItem
from PyQt6.QtGui import QBrush, QColor, QPen
from PyQt6.QtCore import Qt, QRectF

class BlockItem(QGraphicsRectItem):
    def __init__(self, scene, block_type, title, x, y, width=120, height=80):
        super().__init__(x, y, width, height)
        self.x = x
        self.y = y
        self.scene = scene  # Pasar la escena como argumento y asignarla a self.scene
        self.block_type = block_type
        self.is_dragging = False
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
        blocksDesing.drawPointsConnections(self, block_type, x, y, width)
        '''self.connection_points = {
            'condition': QPointF(x + 10, y + self.header_height + 10),
            'true': QPointF(x + width - 10, y + self.header_height + 5),
            'false': QPointF(x + width - 10, y + self.header_height + 25)
        }

        # Draw connection points and labels
        self.add_connection_point('condition', "condition")
        self.add_connection_point('true', "true")
        self.add_connection_point('false', "false")'''

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

    #Aun no funciona dibujar los puntos de conexion
    def add_connection_point(self, point_name, label):
        point = self.connection_points[point_name]
        circle = QGraphicsEllipseItem(point.x() - 3, point.y() - 3, 6, 6, self)
        circle.setPen(QPen(Qt.GlobalColor.red))
        circle.setBrush(QBrush(Qt.GlobalColor.blue))
        #self.scene.addItem(circle)
        
        text = QGraphicsTextItem(label, self)
        text.setDefaultTextColor(Qt.GlobalColor.white)
        text.setPos(point.x() + 5, point.y() - 8)
        #self.scene.addItem(text)
    
    def paint(self, painter, option, widget):
        # Draw the main rectangle
        super().paint(painter, option, widget)
        # Draw the header
        painter.setBrush(self.header_brush)
        painter.drawRect(self.header_rect)

    # Override mouse press event
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            if self.header_rect.contains(event.pos()):
                self.setCursor(Qt.CursorShape.ClosedHandCursor)
                self.is_dragging = True

    # Override mouse move event
    def mouseMoveEvent(self, event):
        if self.is_dragging and event.buttons() & Qt.MouseButton.LeftButton:
            new_pos = event.scenePos()
            self.setPos(new_pos.x() - self.x, new_pos.y() - self.y)

    # Override mouse release event
    def mouseReleaseEvent(self, event):
        if self.header_rect.contains(event.pos()):
            self.setCursor(Qt.CursorShape.ClosedHandCursor)
        else:
            self.setCursor(Qt.CursorShape.ArrowCursor)
        self.is_dragging = False