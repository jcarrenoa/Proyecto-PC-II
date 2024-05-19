from App.Blocks.Block import BlockItem
from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QWidget, QMenu, QLineEdit, QTextEdit, QMenuBar, QGraphicsScene, QGraphicsView
from PyQt6 import QtCore, QtGui

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Visual Scripting")
        self.resize(1112, 688)
        self.centralwidget = QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.icon_only_widget = QWidget(parent=self.centralwidget)
        self.icon_only_widget.setGeometry(QtCore.QRect(0, 0, 151, 661))
        self.icon_only_widget.setStyleSheet("QWidget {\n"
"    background-color: rgb(118, 171, 174);\n"
"}\n"
"\n"
"QPushButton {\n"
"  min-width: 70px;\n"
"  height: 40px;\n"
"  color: #fff;\n"
"  padding: 5px 10px;\n"
"  font-weight: bold;\n"
"  cursor: pointer;\n"
"  transition: all 0.3s ease;\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  outline: none;\n"
"  border-radius: 10px;\n"
"  border: 2px solid #adb5bd;\n"
"  background: #adb5bd;\n"
"}\n"
"QPushButton:hover {\n"
"  background: #fff;\n"
"  color: #adb5bd\n"
"}\n"
"\n"
"QLineEdit {\n"
"\n"
"}\n"
"")
        self.icon_only_widget.setObjectName("icon_only_widget")
        self.add_script = QPushButton(parent=self.icon_only_widget)
        self.add_script.setGeometry(QtCore.QRect(20, 630, 111, 24))
        self.add_script.setObjectName("add_script")
        self.label_script = QLabel(parent=self.icon_only_widget)
        self.label_script.setGeometry(QtCore.QRect(30, 10, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(14)
        font.setBold(True)
        self.label_script.setFont(font)
        self.label_script.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_script.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_script.setObjectName("label_script")
        self.text_script_add = QLineEdit(parent=self.icon_only_widget)
        self.text_script_add.setGeometry(QtCore.QRect(10, 600, 131, 22))
        self.text_script_add.setObjectName("text_script_add")
        self.widget = QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(150, 0, 811, 661))
        self.widget.setStyleSheet("QWidget {\n"
"    background-color: rgb(49, 54, 63);\n"
"}\n"
"\n"
"QTextEdit {\n"
"    \n"
"    border-color: rgb(118, 171, 174);\n"
"}")
        self.widget.setObjectName("widget")
        self.widget_cmd = QWidget(parent=self.widget)
        self.widget_cmd.setGeometry(QtCore.QRect(10, 430, 791, 221))
        self.widget_cmd.setObjectName("widget_cmd")
        self.cmd = QTextEdit(parent=self.widget_cmd)
        self.cmd.setGeometry(QtCore.QRect(10, 10, 771, 201))
        self.cmd.setReadOnly(True)
        self.cmd.setObjectName("cmd")
        self.widget_view = QWidget(parent=self.widget)
        self.widget_view.setGeometry(QtCore.QRect(19, 19, 771, 401))
        self.widget_view.setObjectName("widget_view")
        self.work_area = QGraphicsView(parent=self.widget_view)
        self.work_area.setGeometry(QtCore.QRect(5, 1, 761, 391))
        self.work_area.setObjectName("work_area")
        self.graphics_scene = QGraphicsScene()
        self.work_area.setScene(self.graphics_scene)
        self.icon_only_widget_2 = QWidget(parent=self.centralwidget)
        self.icon_only_widget_2.setGeometry(QtCore.QRect(960, 0, 151, 661))
        self.icon_only_widget_2.setStyleSheet("QWidget {\n"
"    background-color: rgb(118, 171, 174);\n"
"}\n"
"\n"
"QPushButton {\n"
"  min-width: 70px;\n"
"  height: 40px;\n"
"  color: #fff;\n"
"  padding: 5px 10px;\n"
"  font-weight: bold;\n"
"  cursor: pointer;\n"
"  transition: all 0.3s ease;\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  outline: none;\n"
"  border-radius: 10px;\n"
"  border: 2px solid #adb5bd;\n"
"  background: #adb5bd;\n"
"}\n"
"QPushButton:hover {\n"
"  background: #fff;\n"
"  color: #adb5bd\n"
"}\n"
"")
        self.icon_only_widget_2.setObjectName("icon_only_widget_2")
        self.add_variable = QPushButton(parent=self.icon_only_widget_2)
        self.add_variable.setGeometry(QtCore.QRect(20, 630, 111, 24))
        self.add_variable.setObjectName("add_variable")
        self.label_variable = QLabel(parent=self.icon_only_widget_2)
        self.label_variable.setGeometry(QtCore.QRect(40, 10, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(14)
        font.setBold(True)
        self.label_variable.setFont(font)
        self.label_variable.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_variable.setObjectName("label_variable")
        self.text_variable_add = QLineEdit(parent=self.icon_only_widget_2)
        self.text_variable_add.setGeometry(QtCore.QRect(10, 600, 131, 22))
        self.text_variable_add.setObjectName("text_variable_add")
        self.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(parent=self)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1112, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QMenu(parent=self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuBlock = QMenu(parent=self.menuBar)
        self.menuBlock.setObjectName("menuBlock")
        self.setMenuBar(self.menuBar)
        self.actionImport = QtGui.QAction(parent=self)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtGui.QAction(parent=self)
        self.actionExport.setObjectName("actionExport")
        self.actionSearch = QtGui.QAction(parent=self)
        self.actionSearch.setObjectName("actionSearch")
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)
        self.menuBlock.addAction(self.actionSearch)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuBlock.menuAction())

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.work_area.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.work_area.customContextMenuRequested.connect(self.show_context_menu)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_script.setText(_translate("MainWindow", "Add"))
        self.label_script.setText(_translate("MainWindow", "Scripts"))
        self.add_variable.setText(_translate("MainWindow", "Add"))
        self.label_variable.setText(_translate("MainWindow", "Variable"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuBlock.setTitle(_translate("MainWindow", "Block"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionSearch.setText(_translate("MainWindow", "Search"))

    def show_context_menu(self, pos):
        context_menu = QMenu(self)

        # Lista de bloques a añadir
        block_types = ["If", "On_Start", "On_Update", "cycle", "set_var", "set_arr", "call_var", "log", "branch", "compare", "less_equal", "greater_equal", "for_iter", "add", "sub", "mult", "div", "div_int", "mod", "append_arr"]
        
        # Crear acciones para cada bloque
        for block_type in block_types:
            action = QtGui.QAction(block_type, self)
            action.triggered.connect(lambda checked, bt=block_type: self.add_block(bt, pos))
            context_menu.addAction(action)

        context_menu.exec(self.work_area.mapToGlobal(pos))

    def add_block(self, block_type, pos):
        # Convertir la posición del clic a coordenadas de la escena
        scene_pos = self.work_area.mapToScene(pos)
        block = BlockItem(self.graphics_scene, block_type, block_type, scene_pos.x(), scene_pos.y())  # Pasar self.graphics_scene como argumento
        self.graphics_scene.addItem(block)