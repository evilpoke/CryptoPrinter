from PyQt5 import QtWidgets, QtGui, QtCore
from HelperClasses import Translator
import math

class IndicatorGraphicView(QtWidgets.QGraphicsView):

    def __init__(self, *args, **kwargs):
        super(IndicatorGraphicView,self).__init__(*args,**kwargs)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.setScene(self.scene)
        #self.setSceneRect(0,0, 80, 375)      
        self.mainScene_y = 0.85
        self.xPos = 45
        self.space = (1-self.mainScene_y) / 2  

        self.height = 375
        self.width = 95

        self.ytrans = Translator(150,-150,self.space*self.height,(1-self.space)*self.height)
        self.greentrans = Translator(150,-150,0,255)
        self.redtrans = Translator(-150,150,0,255)

        self.currentDot = QtWidgets.QGraphicsRectItem()
        self.plot_frame()
        self.scene.addItem(self.currentDot)

    def plot_frame(self):
        self.scene.addLine(0, self.height, 0, 0)
        self.scene.addLine(self.width, self.height, self.width, 0)
        self.scene.addLine(0, 0, self.width, 0)
        self.scene.addLine(0, self.height, self.width, self.height)
        pen = QtGui.QPen()
        pen.setWidth(2)
        self.scene.addLine(self.xPos, self.ytrans.t(100), self.xPos, self.ytrans.t(-100),pen)
        y = self.ytrans.t(100)
        self.scene.addLine(self.xPos+10, y, self.xPos-10, y)
        y = self.ytrans.t(-100)
        self.scene.addLine(self.xPos+10, y, self.xPos-10, y)

        pen.setColor(QtGui.QColor(255,0,0))
        y = self.ytrans.t(150) - 10
        self.scene.addLine(self.xPos, self.ytrans.t(100), self.xPos, y, pen)
        self.scene.addLine(self.xPos+5, y, self.xPos-5, y,pen)

        pen.setColor(QtGui.QColor(0,255,0))
        y = self.ytrans.t(-150) + 10
        self.scene.addLine(self.xPos, self.ytrans.t(-100), self.xPos, y,pen)
        self.scene.addLine(self.xPos+5, y, self.xPos-5, y,pen)
        #self.scene.addLine(self.xPos[0], self.ytrans.t(150), self.xPos[0], self.ytrans.t(-150))

    def plot_currentIndicator(self, indicatordata):
        sign = lambda x: indicatordata and (1, -1) [indicatordata<0]
        if abs(indicatordata) > 150:
            indicatordata = 150 * sign
        yPos = self.ytrans.t(indicatordata)
        self.currentDot.setRect(self.xPos - 10, yPos - 5, 20, 10)
        pen = QtGui.QPen()
        brush = QtGui.QBrush()
        pen.setWidth(3)
        color = QtGui.QColor(self.redtrans.t(indicatordata), self.greentrans.t(indicatordata), 0)    
        pen.setColor(color)
        brush.setColor(color)
        self.currentDot.setPen(pen)
        self.currentDot.setBrush(brush)
