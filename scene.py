import sys
from PyQt5.QtCore import Qt, QSize,QPoint
from PyQt5.QtGui import QIcon,QBrush,QPen,QColor
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
    def mouseMoveEvent(self, event):
        self.end=event.scenePos()
    def mouseReleaseEvent(self, event):
        self.end=event.scenePos()
        if(self.tool == "line"):
            line=QGraphicsLineItem(
                self.begin.x(),self.begin.y(),
                self.end.x(),self.end.y()
            )
            line.setPen(self.pen)
            self.addItem(line)
        if(self.tool == "rect"):
            rect=QGraphicsRectItem(
                self.begin.x(),self.begin.y(),
                self.end.x()-self.begin.x(),
                self.end.y()-self.begin.y()
            )
            rect.setPen(self.pen)
            rect.setBrush(self.brush)
            self.addItem(rect)
        if(self.tool == "ellipse"):
            ellipse=QGraphicsEllipseItem(
                self.begin.x(),self.begin.y(),
                self.end.x()-self.begin.x(),
                self.end.y()-self.begin.y()
            )
            ellipse.setPen(self.pen)
            ellipse.setBrush(self.brush)
            self.addItem(ellipse)
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

    def itemsToData(self):
        itemsToSave=[]
        for item in self.items():
            data = {}
            #Looking for a Shape
            if isinstance(item, QGraphicsLineItem):
                data["type"]= "line"
                data["x1"]= item.line().x1()
                data["y1"]= item.line().y1()
                data["x2"]= item.line().x2()
                data["y2"]= item.line().y2()
            if isinstance(item, QGraphicsRectItem):
                data["type"]= "rect"
                data["x"]= item.rect().x()
                data["y"]= item.rect().y()
                data["h"]= item.rect().width()
                data["w"]= item.rect().height()
            if isinstance(item, QGraphicsEllipseItem):
                data["type"] = "ellipse"
                data["x"] = item.rect().x()
                data["y"] = item.rect().y()
                data["h"] = item.rect().width()
                data["w"] = item.rect().height()
            # if isinstance(item, QGraphicsTextItem):
            #     data["type"] = "text"
            #     data["content"] = item.text()
            #     data["x"] = item.x()
            #     data["y"] = item.y()
            #Looking for an Attribute
            if hasattr(item, "pen"):
                data["pen"]= {
                    "color": item.pen().color().rgba()
                }
            if hasattr(item, "brush"):
                data["brush"]= {
                    "color": item.brush().color().rgba()
                }
            itemsToSave.append(data)
        print(itemsToSave)
        return itemsToSave

    def dataToItems(self,data):
        for dataItem in data :
            #Find the current type of shape to load
            itemType = dataItem["type"]
            if itemType == "line":
                x1 = dataItem["x1"]
                y1 = dataItem["y1"]
                x2 = dataItem["x2"]
                y2 = dataItem["y2"]
                color = dataItem["pen"]["color"]
                item = self.addLine(x1, y1, x2, y2)
            if itemType == "rect":
                x = dataItem["x"]
                y = dataItem["y"]
                w = dataItem["w"]
                h = dataItem["h"]
                color = dataItem["pen"]["color"]
                fill = dataItem["brush"]["color"]
                item = self.addRect(x, y, h, w)
            if itemType == "ellipse":
                x = dataItem["x"]
                y = dataItem["y"]
                w = dataItem["w"]
                h = dataItem["h"]
                color = dataItem["pen"]["color"]
                fill = dataItem["brush"]["color"]
                item = self.addEllipse(x, y, h, w)
            # if itemType == "text":
            #     content = dataItem["content"]
            #     x = dataItem["x"]
            #     y = dataItem["y"]
            #Load attributes to the current shape to be displayed
            if "pen" in dataItem :
                pen = QPen(QColor(dataItem["pen"]["color"]))
                item.setPen(pen)
            if "brush" in dataItem :
                pen = QBrush(QColor(dataItem["brush"]["color"]))
                item.setBrush(pen)

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
