import sys
from PyQt5.QtCore import Qt, QSize,QPoint
from PyQt5.QtGui import QIcon,QBrush,QPen
from PyQt5.QtWidgets import QApplication,QMainWindow, \
QGraphicsScene, QGraphicsView,QGraphicsItem, QGraphicsRectItem, \
 QGraphicsEllipseItem, QGraphicsLineItem, QGraphicsPolygonItem, \
  QGraphicsTextItem, QDialog, QLineEdit, QPushButton

class Scene (QGraphicsScene) :
    def __init__(self,*args,**kwargs):
        super(Scene, self).__init__(*args,**kwargs)
        self.pen=QPen()
        self.pen.setWidth(2)
        self.pen.setColor(Qt.red)
        self.brush=QBrush(Qt.green)
        self.tool = "rect"
        self.create()
        self.begin,self.end=QPoint(0,0),QPoint(0,0)
        self.pressed = False
        self.line = QGraphicsLineItem(
                    self.begin.x(),self.begin.y(),
                    self.end.x(),self.end.y()
                    )
        self.rect=QGraphicsRectItem(
                    self.begin.x(),self.begin.y(),
                    self.end.x()-self.begin.x(),
                    self.end.y()-self.begin.y()
                )
        self.ellipse=QGraphicsEllipseItem(
                    self.begin.x(),self.begin.y(),
                    self.end.x()-self.begin.x(),
                    self.end.y()-self.begin.y()
                )

    def create(self) :
        text=self.addText("Hello World !") # add item in Model 
        text.setPos(0,0)
        text.setVisible(False)
        rect=QGraphicsRectItem(50,100,200,50)
        rect.setFlag(QGraphicsItem.ItemIsMovable)
        rect.setPen(self.pen)
        rect.setBrush(self.brush)
        self.addItem(rect)                # add item in Model 
    def set_pen_color(self,color) :
        self.pen.setColor(color)
    def set_brush_color(self,color) :
        self.brush.setColor(color)
    def set_tool(self,tool):
        self.tool = tool

    def mousePressEvent(self, event):
        self.begin=self.end=event.scenePos()
        self.pressed = True
    def mouseMoveEvent(self, event):
        self.end=event.scenePos()
        pen = QPen(Qt.black, 2, Qt.DashLine)
        if (self.pressed) : 
            if(self.tool == "line"):
                self.removeItem(self.line)
                self.line=QGraphicsLineItem(
                    self.begin.x(),self.begin.y(),
                    self.end.x(),self.end.y()
                )
                self.line.setPen(pen)
                self.addItem(self.line)
            if(self.tool == "rect"):
                self.removeItem(self.rect)
                self.rect=QGraphicsRectItem(
                    self.begin.x(),self.begin.y(),
                    self.end.x()-self.begin.x(),
                    self.end.y()-self.begin.y()
                )
                self.rect.setPen(pen)
                self.addItem(self.rect)
            if(self.tool == "ellipse"):
                self.removeItem(self.ellipse)
                self.ellipse=QGraphicsEllipseItem(
                    self.begin.x(),self.begin.y(),
                    self.end.x()-self.begin.x(),
                    self.end.y()-self.begin.y()
                )
                self.ellipse.setPen(pen)
                self.addItem(self.ellipse)
    def mouseReleaseEvent(self, event):
        self.end=event.scenePos()
        if(self.tool == "line"):
            line=QGraphicsLineItem(
                self.begin.x(),self.begin.y(),
                self.end.x(),self.end.y()
            )
            line.setPen(self.pen)
            self.addItem(line)
            self.pressed = False
        if(self.tool == "rect"):
            rect=QGraphicsRectItem(
                self.begin.x(),self.begin.y(),
                self.end.x()-self.begin.x(),
                self.end.y()-self.begin.y()
            )
            rect.setPen(self.pen)
            rect.setBrush(self.brush)
            self.addItem(rect)
            self.pressed = False
        if(self.tool == "ellipse"):
            ellipse=QGraphicsEllipseItem(
                self.begin.x(),self.begin.y(),
                self.end.x()-self.begin.x(),
                self.end.y()-self.begin.y()
            )
            ellipse.setPen(self.pen)
            ellipse.setBrush(self.brush)
            self.addItem(ellipse)
            self.pressed = False
        if(self.tool == "polygon"):
            polygon=QGraphicsPolygonItem(
                self.begin.x(),self.begin.y(),
                self.end.x()-self.begin.x(),
                self.end.y()-self.begin.y()
            )
            polygon.setPen(self.pen)
            polygon.setBrush(self.brush)
            self.addItem(polygon)
        if(self.tool == "text"):
            d = QDialog()
            line = QLineEdit(d)
            line.move(10,10)
            b = QPushButton("Confirmer", d)
            b.move(175,10)
            b.clicked.connect(d.close)
            d.resize(300,100)
            d.setWindowTitle("Text")
            d.exec()
            text=QGraphicsTextItem(line.text())
            text.setPos(self.begin.x(), self.begin.y())
            self.addItem(text)

if __name__=="__main__" :
    app=QApplication(sys.argv)
    mw=QMainWindow()
    mw.setGeometry(400,300,300,400)
    view=QGraphicsView()   # View 
    scene=Scene(mw)        # Model (graphics item container)
    view.setScene(scene)   #  View-Model connection
    mw.setCentralWidget(view) #  Mainwindow Client Area
    mw.show()
    app.exec_()
