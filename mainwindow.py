# code : https://www.learnpyqt.com/tutorials/actions-toolbars-menus
# icones https://p.yusukekamiyamane.com

import sys,json,os
from PyQt5.QtCore import Qt, QSize, QFile, QIODevice
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, \
QToolBar,QAction,QStatusBar,QGraphicsView, \
QLabel,QVBoxLayout,QDialog, QDialogButtonBox, \
QColorDialog, QMenu,QMessageBox, QFileDialog, QLineEdit, QPushButton

from scene import Scene

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("CAI-P21 : Editeur graphique")
        self.create_scene()
        self.create_actions()
        self.create_toolbars()
        self.create_menus()
        self.resize(1080,800)
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
        name="Pen Width" 
        self.action_style_pen_width=QAction(QIcon('Icons/pen_width.png'), name, self)
        self.action_style_pen_width.setStatusTip("Select Pen width")
        self.action_style_pen_width.triggered.connect(lambda status,selection=name : self.on_triggered_action(status,selection))
        name="Pen Color" 
        self.action_style_pen_color=QAction(QIcon('Icons/colorize.png'), name, self)
        self.action_style_pen_color.setStatusTip("Select Pen color")
        self.action_style_pen_color.triggered.connect(lambda status,selection=name : self.on_triggered_action(status,selection))
        name="Solid Line" 
        self.action_style_solid_line=QAction(QIcon('Icons/tool_line.png'), name, self)
        self.action_style_solid_line.setStatusTip("Create a solid line")
        self.action_style_solid_line.setCheckable(True)
        self.action_style_solid_line.triggered.connect(lambda status,selection=name : self.on_triggered_action(status,selection))
        name="Dot Line" 
        self.action_style_dot_line=QAction(QIcon('Icons/dot_line.png'), name, self)
        self.action_style_dot_line.setStatusTip("Create a dot line")
        self.action_style_dot_line.setCheckable(True)
        self.action_style_dot_line.triggered.connect(lambda status,selection=name : self.on_triggered_action(status,selection))
        name="Dash Line" 
        self.action_style_dash_line=QAction(QIcon('Icons/dash_line.png'), name, self)
        self.action_style_dash_line.setStatusTip("Create a dash line")
        self.action_style_dash_line.setCheckable(True)
        self.action_style_dash_line.triggered.connect(lambda status,selection=name : self.on_triggered_action(status,selection))

        name="Brush Color" 
        self.action_style_brush_color=QAction(QIcon('Icons/colorize.png'), name, self)
        self.action_style_brush_color.setStatusTip("Select Brush color")
        self.action_style_brush_color.triggered.connect(lambda status,selection=name : self.on_triggered_action(status,selection))
        
        name="Brush Solid Pattern" 
        self.action_style_brush_solid=QAction(QIcon('Icons/solid_pattern.png'), name, self)
        self.action_style_brush_solid.setStatusTip("Select brush solid pattern")
        self.action_style_brush_solid.setCheckable(True)
        self.action_style_brush_solid.triggered.connect(lambda status,selection=name : self.on_triggered_action(status,selection))
        name="Brush Cross Pattern" 
        self.action_style_brush_cross=QAction(QIcon('Icons/cross_pattern.png'), name, self)
        self.action_style_brush_cross.setStatusTip("Select brush cross pattern")
        self.action_style_brush_cross.setCheckable(True)
        self.action_style_brush_cross.triggered.connect(lambda status,selection=name : self.on_triggered_action(status,selection))
        name="Brush Dense2 Pattern" 
        self.action_style_brush_dense2=QAction(QIcon('Icons/dense2_pattern.png'), name, self)
        self.action_style_brush_dense2.setStatusTip("Select brush dense2 pattern")
        self.action_style_brush_dense2.setCheckable(True)
        self.action_style_brush_dense2.triggered.connect(lambda status,selection=name : self.on_triggered_action(status,selection))
        name="Brush Horizontal Pattern" 
        self.action_style_brush_hor=QAction(QIcon('Icons/hor_pattern.png'), name, self)
        self.action_style_brush_hor.setStatusTip("Select brush horizontal pattern")
        self.action_style_brush_hor.setCheckable(True)
        self.action_style_brush_hor.triggered.connect(lambda status,selection=name : self.on_triggered_action(status,selection))
        name="Brush Vertical Pattern" 
        self.action_style_brush_ver=QAction(QIcon('Icons/ver_pattern.png'), name, self)
        self.action_style_brush_ver.setStatusTip("Select brush vertical pattern")
        self.action_style_brush_ver.setCheckable(True)
        self.action_style_brush_ver.triggered.connect(lambda status,selection=name : self.on_triggered_action(status,selection))
        
        name="Rectangle"
        self.action_rectangle=QAction(QIcon('Icons/tool_rectangle.png'), name, self)
        self.action_rectangle.setStatusTip("Create a rectangle")
        self.action_rectangle.setCheckable(True)
        self.action_rectangle.triggered.connect(lambda status,selection=name :
                                                self.on_triggered_action(status,selection))
        name="Ellipse"
        self.action_ellipse=QAction(QIcon('Icons/tool_ellipse.png'), name, self)
        self.action_ellipse.setStatusTip("Create an ellipse")
        self.action_ellipse.setCheckable(True)
        self.action_ellipse.triggered.connect(lambda status,selection=name :
                                                self.on_triggered_action(status,selection))
        name="Line"
        self.action_line=QAction(QIcon('Icons/tool_line.png'), name, self)
        self.action_line.setStatusTip("Create a line")
        self.action_line.setCheckable(True)
        self.action_line.triggered.connect(lambda status,selection=name :
                                                self.on_triggered_action(status,selection))
        name="Polygon"
        self.action_polygon=QAction(QIcon('Icons/tool_polygon.png'), name, self)
        self.action_polygon.setStatusTip("Create a polygon")
        self.action_polygon.setCheckable(True)
        self.action_polygon.triggered.connect(lambda status,selection=name :
                                                self.on_triggered_action(status,selection))
        name="Text"
        self.action_text=QAction(QIcon('Icons/tool_text.png'), name, self)
        self.action_text.setStatusTip("Create a text")
        self.action_text.setCheckable(True)
        self.action_text.triggered.connect(lambda status,selection=name :
                                                self.on_triggered_action(status,selection))

        name="About Us"
        self.action_file_aboutus=QAction(QIcon('Icons/tool_text.png'), name, self)
        self.action_file_aboutus.setStatusTip("About Us")
        self.action_file_aboutus.setCheckable(True)
        self.action_file_aboutus.triggered.connect(lambda status,selection=name : self.on_triggered_action(status,selection))
        name="About Qt"
        self.action_file_aboutqt=QAction(QIcon('Icons/tool_text.png'), name, self)
        self.action_file_aboutqt.setStatusTip("About Qt")
        self.action_file_aboutqt.setCheckable(True)
        self.action_file_aboutqt.triggered.connect(lambda status,selection=name : self.on_triggered_action(status,selection))
        name="README"
        self.action_file_readme=QAction(QIcon('Icons/tool_text.png'), name, self)
        self.action_file_readme.setStatusTip("README")
        self.action_file_readme.setCheckable(True)
        self.action_file_readme.triggered.connect(lambda status,selection=name : self.on_triggered_action(status,selection))
    def create_toolbars(self) :
        self.toolbar=QToolBar("Main Toolbar")
        self.addToolBar(self.toolbar)
        self.toolbar.setIconSize(QSize(16,16))
        self.setStatusBar(QStatusBar(self))

        self.toolbar.addAction(self.action_file_new)
        self.toolbar.addAction(self.action_file_open)
        self.toolbar.addAction(self.action_file_exit)

        self.toolbar.addAction(self.action_line)
        self.toolbar.addAction(self.action_rectangle)
        self.toolbar.addAction(self.action_ellipse)
        self.toolbar.addAction(self.action_polygon)
        self.toolbar.addAction(self.action_text)
    def create_menus(self) :
        menubar=self.menuBar()
        self.menu_file = menubar.addMenu("&File")
        self.menu_style = menubar.addMenu("&Style")
        self.menu_tools = menubar.addMenu("&Tools")
        self.menu_help = menubar.addMenu("&Help")

        self.pen_style = QMenu('Pen',self)
        self.menu_style.addMenu(self.pen_style)
        self.pen_line = QMenu('Pen Line', self)
        self.pen_style.addMenu(self.pen_line)

        self.brush_style = QMenu('Brush',self)
        self.menu_style.addMenu(self.brush_style)
        self.brush_fill = QMenu('Brush Fill', self)
        self.brush_style.addMenu(self.brush_fill)
        
        self.menu_file.addAction(self.action_file_new)
        self.menu_file.addAction(self.action_file_open)
        self.menu_file.addAction(self.action_file_save)
        self.menu_file.addAction(self.action_file_exit)

        self.pen_style.addAction(self.action_style_pen_color)
        self.pen_style.addAction(self.action_style_pen_width)
        self.pen_line.addAction(self.action_style_solid_line)
        self.pen_line.addAction(self.action_style_dash_line)
        self.pen_line.addAction(self.action_style_dot_line)

        self.brush_style.addAction(self.action_style_brush_color)
        self.brush_fill.addAction(self.action_style_brush_solid)
        self.brush_fill.addAction(self.action_style_brush_cross)
        self.brush_fill.addAction(self.action_style_brush_dense2)
        self.brush_fill.addAction(self.action_style_brush_hor)
        self.brush_fill.addAction(self.action_style_brush_ver)

        self.menu_tools.addAction(self.action_line)
        self.menu_tools.addAction(self.action_rectangle)
        self.menu_tools.addAction(self.action_ellipse)
        self.menu_tools.addAction(self.action_polygon)
        self.menu_tools.addAction(self.action_text)

        self.menu_help.addAction(self.action_file_aboutus)
        self.menu_help.addAction(self.action_file_aboutqt)
        self.menu_help.addAction(self.action_file_readme)


    def on_triggered_action(self,status,selection):
        print("status:",status,", selection:",selection)
        if selection=="Exit" :
            self.exit()
        elif selection=="New" :
            self.new()
        elif selection=="Save As" :
            self.save()

        elif selection=="Pen Color" :
            color=self.style_color()
            if color :
                self.scene.set_pen_color(color)
        elif selection=="Pen Width":
            d = QDialog()
            line = QLineEdit(d)
            line.move(10,10)
            b = QPushButton("Confirm", d)
            b.move(175,10)
            b.clicked.connect(d.close)
            d.resize(300,100)
            d.setWindowTitle("Number of the width")
            d.exec()
            pen_width = 0
            try : 
                pen_width = int(line.text())
            except : 
                d.setWindowTitle("Enter an integer")
            if pen_width!=0:
                self.scene.set_pen_width(pen_width)
        elif selection=="Solid Line": 
            self.action_style_dot_line.setChecked(False)
            self.action_style_dash_line.setChecked(False)
            pen_style = Qt.SolidLine
            if pen_style : 
                self.scene.set_pen_style(pen_style)
        elif selection=="Dot Line": 
            self.action_style_solid_line.setChecked(False)
            self.action_style_dash_line.setChecked(False)
            pen_style = Qt.DotLine
            if pen_style : 
                self.scene.set_pen_style(pen_style)
        elif selection=="Dash Line": 
            self.action_style_dot_line.setChecked(False)
            self.action_style_solid_line.setChecked(False)
            pen_style = Qt.DashLine
            if pen_style : 
                self.scene.set_pen_style(pen_style)

        elif selection=="Brush Color" :
            color=self.style_color()
            if color :
                self.scene.set_brush_color(color)
                
        elif selection== "Brush Solid Pattern" :
            brush_pattern = Qt.SolidPattern
            if brush_pattern : 
                self.scene.set_brush_pattern(brush_pattern)
        elif selection== "Brush Cross Pattern" : 
            brush_pattern = Qt.CrossPattern
            if brush_pattern : 
                self.scene.set_brush_pattern(brush_pattern)
        elif selection== "Brush Dense2 Pattern" : 
            brush_pattern = Qt.Dense2Pattern
            if brush_pattern : 
                self.scene.set_brush_pattern(brush_pattern)
        elif selection== "Brush Horizontal Pattern" :
            brush_pattern = Qt.HorPattern
            if brush_pattern :
                self.scene.set_brush_pattern(brush_pattern)
        elif selection== "Brush Vertical Pattern" : 
            brush_pattern = Qt.VerPattern
            if brush_pattern : 
                self.scene.set_brush_pattern(brush_pattern)

        elif selection=="Line" : 
            self.scene.set_tool("line")
            self.action_rectangle.setChecked(False)
            self.action_ellipse.setChecked(False)
            self.action_polygon.setChecked(False)
            self.action_text.setChecked(False)
        elif selection=="Rectangle" : 
            self.scene.set_tool("rect")
            self.action_line.setChecked(False)
            self.action_ellipse.setChecked(False)
            self.action_polygon.setChecked(False)
            self.action_text.setChecked(False)
        elif selection=="Ellipse" : 
            self.scene.set_tool("ellipse")
            self.action_rectangle.setChecked(False)
            self.action_line.setChecked(False)
            self.action_polygon.setChecked(False)
            self.action_text.setChecked(False)
        elif selection=="Polygon" : 
            self.scene.set_tool("polygon")
            self.action_rectangle.setChecked(False)
            self.action_ellipse.setChecked(False)
            self.action_line.setChecked(False)
            self.action_text.setChecked(False)
        elif selection=="Text" : 
            self.scene.set_tool("text")
            self.action_rectangle.setChecked(False)
            self.action_ellipse.setChecked(False)
            self.action_polygon.setChecked(False)
            self.action_line.setChecked(False)

        elif selection=="New" :
            self.new();
        elif selection=="Save As" :
            self.save();
        elif selection=="Open" :
            self.open();
        elif selection=="About Us" :
            self.help_about_us();
        elif selection=="About Qt" :
            self.help_about_qt();
        elif selection=="README" :
            self.help_about_readme();

    def new(self):
        popup = QMessageBox.warning(self,"New","Are you sure you want to open a new file? \nUnsaved changes will be ignored.", QMessageBox.Ok,QMessageBox.Cancel)
        if(popup == QMessageBox.Ok):
            self.scene.clear()
            self.action_file_new.setCheckable(False)
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
        filename = QFileDialog.getSaveFileName(self, 'Save File As')
        file_to_save = QFile(filename[0])
        if file_to_save.open(QIODevice.WriteOnly):
            data=self.scene.itemsToData()
            file_to_save.write(json.dumps(data).encode("utf-8"))
        file_to_save.close()
        self.action_file_save.setCheckable(False)
    def open(self):
        filename = QFileDialog.getOpenFileName(self,\
            'Open File', os.getcwd())
        file_to_open = QFile(filename[0])
        if file_to_open.open(QFile.ReadOnly | QFile.Text):
            data = json.loads(file_to_open.readAll().data().decode('utf-8'))
            self.scene.clear()
            self.scene.dataToItems(data)
        file_to_open.close()
        self.action_file_open.setCheckable(False)
    def help_about_us(self):
        QMessageBox.information(self, self.tr("About Us"),
                                self.tr("Tony Cuillandre\nJean Bénis\nENIB"))
        self.action_file_aboutus.setCheckable(False)
    def help_about_qt(self):
        QMessageBox.information(self, self.tr("About Qt"),
                                self.tr("Made with Qt library : https://doc.qt.io/qt-5/index.html"))
        self.action_file_aboutqt.setCheckable(False)
    def help_about_readme(self):
        QMessageBox.information(self, self.tr("About this app"),
                                self.tr("README (need to be written)"))
        self.action_file_readme.setCheckable(False)
    def contextMenuEvent(self, event):
        contextMenu = QMenu(self)

        contextMenu.addSeparator()

        contextMenuTools = QMenu("Tools",self)
        contextMenu.addMenu(contextMenuTools)
        lineAct = contextMenuTools.addAction(QIcon('Icons/tool_line.png'),"Line")
        rectAct = contextMenuTools.addAction(QIcon('Icons/tool_rectangle.png'),"Rectangle")
        ellipseAct = contextMenuTools.addAction(QIcon('Icons/tool_ellipse.png'),"Ellipse")
        polygoneAct = contextMenuTools.addAction(QIcon('Icons/tool_polygon.png'),"Polygone")
        contextMenuTools.addSeparator()
        textAct = contextMenuTools.addAction(QIcon('Icons/tool_text.png'), "Text")
        
        contextMenuStyle = QMenu("Style",self)
        contextMenu.addMenu(contextMenuStyle)
        colorPenAct = contextMenuStyle.addAction(QIcon('Icons/colorize.png'),"Color Pen")
        widthPenAct = contextMenuStyle.addAction(QIcon('Icons/pen_width.png'),"Width Pen")
        contextMenuStyle.addSeparator()
        colorBrushAct = contextMenuStyle.addAction(QIcon('Icons/colorize.png'),"Brush Color")

        contextMenu.addSeparator()

        quitAct = contextMenu.addAction("Quit")
        action = contextMenu.exec_(self.mapToGlobal(event.pos()))


        if action==quitAct:
            self.exit()
        elif action==colorPenAct:
            color=self.style_color()
            if color :
                self.scene.set_pen_color(color)
        elif action==widthPenAct:
            d = QDialog()
            line = QLineEdit(d)
            line.move(10,10)
            b = QPushButton("Confirm", d)
            b.move(175,10)
            b.clicked.connect(d.close)
            d.resize(300,100)
            d.setWindowTitle("Number of the width")
            d.exec()
            pen_width = 0
            try : 
                pen_width = int(line.text())
            except : 
                d.setWindowTitle("Enter an integer")
            if pen_width!=0:
                self.scene.set_pen_width(pen_width)
        elif action==colorBrushAct:
            color=self.style_color()
            if color :
                self.scene.set_brush_color(color)

        elif action==lineAct:
            self.scene.set_tool("line")
            self.action_rectangle.setChecked(False)
            self.action_ellipse.setChecked(False)
            self.action_polygon.setChecked(False)
            self.action_text.setChecked(False)
            self.action_line.setChecked(True)
        elif action ==rectAct:
            self.scene.set_tool("rect")
            self.action_rectangle.setChecked(True)
            self.action_ellipse.setChecked(False)
            self.action_polygon.setChecked(False)
            self.action_text.setChecked(False)
            self.action_line.setChecked(False)
        elif action ==ellipseAct:
            self.scene.set_tool("ellipse")
            self.action_rectangle.setChecked(False)
            self.action_ellipse.setChecked(True)
            self.action_polygon.setChecked(False)
            self.action_text.setChecked(False)
            self.action_line.setChecked(False)
        elif action ==polygoneAct:
            self.scene.set_tool("polygon")
            self.action_rectangle.setChecked(False)
            self.action_ellipse.setChecked(False)
            self.action_polygon.setChecked(True)
            self.action_text.setChecked(False)
            self.action_line.setChecked(False)
        elif action==textAct:
            self.scene.set_tool("text")
            self.action_rectangle.setChecked(False)
            self.action_ellipse.setChecked(False)
            self.action_polygon.setChecked(False)
            self.action_text.setChecked(True)
            self.action_line.setChecked(False)

if __name__=="__main__" :
    app=QApplication(sys.argv)
    mw=MainWindow()
    mw.show()
    app.exec_()

