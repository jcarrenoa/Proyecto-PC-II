import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QDockWidget, QListWidget, QWidget, 
    QVBoxLayout, QPushButton, QLabel, QLineEdit, QHBoxLayout, 
    QGroupBox, QRadioButton, QMenu, QGraphicsRectItem, QGraphicsScene, QGraphicsView
)
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QAction




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configurar la ventana principal
        self.setWindowTitle("Visual Scripting")
        self.setGeometry(100, 100, 1200, 800)

        # Crear el área central
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        central_layout = QVBoxLayout(central_widget)

        # Placeholder para el área de trabajo
        self.work_area = QLabel("Work Area", self)
        self.work_area.setStyleSheet("background-color: #333333; color: #FFFFFF; border: 1px solid #FFFFFF;")
        central_layout.addWidget(self.work_area)
        self.work_area.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.work_area.customContextMenuRequested.connect(self.show_context_menu)

        # Habilitar el menú contextual personalizado en el área de trabajo
        self.work_area.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.work_area.customContextMenuRequested.connect(self.show_context_menu)


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

        add_script_button = QPushButton("add new", self)
        dock.setTitleBarWidget(add_script_button)

    def create_settings_panel(self):
        dock = QDockWidget("Settings and Variables", self)
        dock.setAllowedAreas(Qt.DockWidgetArea.RightDockWidgetArea)
        settings_widget = QWidget(dock)
        settings_layout = QVBoxLayout(settings_widget)

        # Algorithm settings
        algorithm_group = QGroupBox("Algorithm", self)
        algorithm_layout = QVBoxLayout()
        data_flow_radio = QRadioButton("Data Flow", self)
        exec_flow_radio = QRadioButton("Exec Flow", self)
        algorithm_layout.addWidget(data_flow_radio)
        algorithm_layout.addWidget(exec_flow_radio)
        algorithm_group.setLayout(algorithm_layout)
        settings_layout.addWidget(algorithm_group)



        # Variables section
        variables_label = QLabel("Variables", self)
        settings_layout.addWidget(variables_label)

        # Add variable input
        add_var_layout = QHBoxLayout()
        add_var_input = QLineEdit(self)
        add_var_button = QPushButton("add", self)
        add_var_layout.addWidget(add_var_input)
        add_var_layout.addWidget(add_var_button)
        settings_layout.addLayout(add_var_layout)

        dock.setWidget(settings_widget)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock)

    def show_context_menu(self, pos: QPoint):
        context_menu = QMenu(self)

        # Lista de bloques a añadir
        block_types = ["On_Start", "On_Update", "cycle", "set_var", "set_arr", "call_var", "log", "branch", "compare", "for_iter", "add", "sub", "mult", "div", "div_int", "mod", "append_arr"]

        # Crear acciones para cada bloque
        for block_type in block_types:
            action = QAction(block_type, self)
            action.triggered.connect(lambda checked, bt=block_type, p=pos: self.add_block(bt, p))
            context_menu.addAction(action)

        context_menu.exec(self.work_area.mapToGlobal(pos))

    def add_block(self, block_type: str, pos: QPoint):
        # Lógica para añadir el bloque a la interfaz en la posición del clic
        block_label = QLabel(block_type, self.work_area)
        block_label.setStyleSheet("background-color: #FFD700; color: #000000; border: 1px solid #000000;")
        block_label.move(pos)
        block_label.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())
