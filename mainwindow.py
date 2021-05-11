# code : https://www.learnpyqt.com/tutorials/actions-toolbars-menus
# icones https://p.yusukekamiyamane.com

import sys
from PyQt5.QtCore import Qt, QSize, QFile, QIODevice
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, \
QToolBar,QAction,QStatusBar,QGraphicsView, \
QLabel,QVBoxLayout,QDialog, QDialogButtonBox, QColorDialog, QMenu, QMessageBox, QFileDialog

from scene import Scene

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("CAI-P21 : Editeur graphique")
        self.create_scene()
        self.create_actions()
        self.create_toolbars()
        self.create_menus()
    def create_scene(self) :
        view=QGraphicsView()
        self.scene=Scene(self)
        view.setScene(self.scene)
        self.setCentralWidget(view)
    def create_actions(self) :
        name="New"
        self.action_file_new =QAction(QIcon('Icons/new.png'), name, self)
        self.action_file_new.setStatusTip("Create new File")
        self.action_file_new.setCheckable(True)
        self.action_file_new.triggered.connect(lambda status,selection=name : self.on_triggered_action(status,selection))
        name="Open"
        self.action_file_open=QAction(QIcon('Icons/open.png'), name, self)
        self.action_file_open.setStatusTip("Open File")
        self.action_file_open.setCheckable(True)
        self.action_file_open.triggered.connect(lambda status,selection=name : self.on_triggered_action(status,selection))
        name="Exit"
        self.action_file_exit=QAction(QIcon('Icons/exit.png'), name, self)
        self.action_file_exit.setStatusTip("Exit application")
        self.action_file_exit.setCheckable(True)
        self.action_file_exit.triggered.connect(lambda status,selection=name : self.on_triggered_action(status,selection))
        name="Save As"
        self.action_file_save=QAction(QIcon('Icons/save_as.png'), name, self)
        self.action_file_save.setStatusTip("Save file")
        self.action_file_save.setCheckable(True)
        self.action_file_save.triggered.connect(lambda status,selection=name : self.on_triggered_action(status,selection))
        name="Pen Color" 
        self.action_style_pen_color=QAction(QIcon('Icons/monkey_on_16x16.png'), name, self)
        self.action_style_pen_color.setStatusTip("Select Pen color")
        self.action_style_pen_color.triggered.connect(lambda status,selection=name : self.on_triggered_action(status,selection))
        name="Brush Color" 
        self.action_style_brush_color=QAction(QIcon('Icons/monkey_on_16x16.png'), name, self)
        self.action_style_brush_color.setStatusTip("Select Brush color")
        self.action_style_brush_color.triggered.connect(lambda status,selection=name : self.on_triggered_action(status,selection))
    def create_toolbars(self) :
        self.toolbar=QToolBar("Main Toolbar")
        self.addToolBar(self.toolbar)
        self.toolbar.setIconSize(QSize(16,16))
        self.toolbar.addAction(self.action_file_new)
        self.toolbar.addAction(self.action_file_open)
        self.toolbar.addAction(self.action_file_exit)
    def create_menus(self) :
        menubar=self.menuBar()
        self.menu_file = menubar.addMenu("&File")
        self.menu_style = menubar.addMenu("&Style")
        self.pen_style = QMenu('Pen',self)
        self.menu_style.addMenu(self.pen_style)
        self.brush_style = QMenu('Brush',self)
        self.menu_style.addMenu(self.brush_style)
        self.menu_file.addAction(self.action_file_new)
        self.menu_file.addAction(self.action_file_open)
        self.menu_file.addAction(self.action_file_save)
        self.menu_file.addAction(self.action_file_exit)
        self.pen_style.addAction(self.action_style_pen_color)
        self.brush_style.addAction(self.action_style_brush_color)
     
    def on_triggered_action(self,status,selection):
        print("status:",status,", selection:",selection)
        if selection=="Exit" :
            self.exit()
        elif selection=="Pen Color" :
            color=self.style_color()
            if color :
                self.scene.set_pen_color(color)
        elif selection=="Brush Color" :
            color=self.style_color()
            if color :
                self.scene.set_brush_color(color)
        elif selection=="New" :
            self.new();
        elif selection=="Save As" :
            self.save();

    def new(self):
        popup = QMessageBox.warning(self,"New","Are you sure you want to open a new file? \nUnsaved changes will be ignored.", QMessageBox.Ok,QMessageBox.Cancel)
        if(popup == QMessageBox.Ok):
            self.scene.clear()
    def exit(self) :
        popup = QMessageBox.warning(self,"Exit","Are you sure you want to exit? \nUnsaved changes will be ignored.",QMessageBox.Ok,QMessageBox.Cancel)
        if(popup == QMessageBox.Ok):
            exit()
    def style_color(self):
        color=QColorDialog.getColor(Qt.yellow,self)
        if color.isValid() :
            print("color :",color)
        else :
            color=None
        return color
    def save(self):
        pass

if __name__=="__main__" :
    app=QApplication(sys.argv)
    mw=MainWindow()
    mw.show()
    app.exec_()

