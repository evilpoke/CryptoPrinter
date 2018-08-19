from PyQt5 import QtWidgets, QtGui, QtCore
import XML_Parser

class DropResponeGraphicView(QtWidgets.QGraphicsView):
    def __init__(self, *args, **kwargs):
        super(DropResponeGraphicView,self).__init__(*args,**kwargs)
        self.setAcceptDrops(True)
        self.lastpath = ""

    def dragEnterEvent(self,e):
        self.removeScene()
        path = e.mimeData().text()
        realpath = self.__checkandreturn_file(path)
        if realpath != "":
            self.lastpath = realpath           
            e.accept()
        else:
            self.lastpath = ""
            e.ignore()
            self.__setButtonState(False)
   
    def dropEvent(self, e):
        if self.lastpath != "":
            values = XML_Parser.get_simpledata_from_xmlfile(self.lastpath)
            self.addScene()
            for key in values:
                TextandIconPair(self.scene, key, values[key])
            self.__setButtonState(True)
        else:
            self.__setButtonState(False)

    def __setButtonState(self, state):
        parent = self
        for _ in range(5):
            parent = parent.parentWidget()
        parent.setButtonState(state, self.lastpath)

    def removeScene(self):
        self.setScene(None)

    def addScene(self):
        self.scene = QtWidgets.QGraphicsScene(self)
        self.setScene(self.scene)

    def __checkandreturn_file(self, path):
        if path[:4] == 'file':
            realpath = path[7:]
            ending = path[-4:]
            if ending == '.xml':
                return realpath
            else:
                print("Invalid file")
                return ""
        else:   
            print("Invalid file")
            return ""

class TextandIconPair():
    def __init__(self, scene, type, text):
        newtext = QtWidgets.QGraphicsTextItem()
        newtext.setPlainText(type + ": " + str(text))
        font = QtGui.QFont()
        if(type == "symbol"): 
            newtext.setPos(0,50)
            font.setPointSize(30)
        if(type == "version"): 
            newtext.setPos(0,100)
            font.setPointSize(10)
        if(type == "interval"): 
            newtext.setPos(0,130)
            font.setPointSize(20)
        if(type == "indicatorcounter"): 
            newtext.setPos(0,160)
            font.setPointSize(20)
        newtext.setFont(font)
        scene.addItem(newtext)
    
