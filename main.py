import sys
import queue
import time
from Ui_mainUI import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore, QtGui

import XML_Parser
import Indicator_Manager
import Candle_Manager
import InstanceHolder
import Trading_Manager
import Trade_Logger

class MainWindow(Ui_MainWindow,QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args,**kwargs)
        self.setupUi(self)
        self.usepath_button.pressed.connect(self.setMainPage)
        self.start_button.pressed.connect(self.startTrading)
        self.xmlurl = ""
        InstanceHolder.add_instance(self, 'MainWindow')
        self.workqueue = queue.Queue()
        self.queueTimer = QtCore.QTimer()
        self.queueTimer.timeout.connect(self.on_timertick)
        self.queueTimer.start(100)
        self.show()

    def setButtonState(self,state, xmlurl):
        self.usepath_button.setEnabled(state)
        self.xmlurl = xmlurl

    def setMainPage(self):
        self.stackedWidget.setCurrentIndex(1)
        Indicator_Manager.load_indicators()
        indicatorValues = XML_Parser.get_indicators_from_xmlfile(self.xmlurl)
        for indicator in indicatorValues:
            name = indicator['name']
            for key in indicator:       
                if key != 'name': 
                    Indicator_Manager.set_indicator(name, key, indicator[key])
            Indicator_Manager.add_to_active(name)

    def on_timertick(self):
        if self.workqueue.empty() is not True:
            task = self.workqueue.get()
            if task == 'new_price':
                Trading_Manager.on_newprice()
                self.plot_currentIndicator()
            if task == 'new_candle':
                Trading_Manager.on_newcandle()
    
    def add_queueitem(self, task):
        self.workqueue.put(task)

    def startTrading(self):
        symbol, interval = XML_Parser.get_symbolandinterval(self.xmlurl)
        Trading_Manager.startTrading(symbol, interval)

    def plot_currentIndicator(self):
        currentIndicator = Indicator_Manager.get_activeindicatordata(1)[0]
        self.indicator_graphicView.plot_currentIndicator(currentIndicator)

    def plot_Indicator(self):
        pass

if __name__ == '__main__':  
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("CryptoPrinter") 
    Trading_Manager.instantiate_newexchange("bitmex","","")
    Trade_Logger.clear_log()
    window = MainWindow()
    app.exec_()
    