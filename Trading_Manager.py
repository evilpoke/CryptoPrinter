import Candle_Manager
import Indicator_Manager
import Trade_Logger
import API_Manager

import numpy as np

__trailingvalue = {'trailing': False, 'trailvalue': 5, 'lasttrail': 0}

__tradingdata = {'lastpos': 0, 'currentpos': 0}

realTrading = False

def startTrading(symbol, interval):
    Candle_Manager.load_candles(symbol, interval=interval)
    API_Manager.open_klinesstream(symbol, interval=interval)  

def on_newcandle():
    __check_indicatordata()

def __check_indicatordata():
    indicatordata = Indicator_Manager.get_activeindicatordata(1)[0]
    currentIndicator = abs(indicatordata)
    __tradingdata['currentpos'] = int(np.sign(indicatordata))
    if currentIndicator >= 100 and __trailingvalue['trailing'] is not True and __tradingdata['lastpos'] != __tradingdata['currentpos']:
        __trailingvalue['trailing'] = True
        __trailingvalue['lasttrail'] = currentIndicator
        print("Started trailing")
    if __trailingvalue['trailing']:
        __trail(currentIndicator)

def __trail(currentValue):
    if currentValue > __trailingvalue['lasttrail']:
        __trailingvalue['lasttrail'] = currentValue
    if currentValue < __trailingvalue['lasttrail'] - __trailingvalue['trailvalue']:   
        __trailingvalue['trailing'] = False
        __tradingdata['lastpos'] = __tradingdata['currentpos']
        side = ""
        if __tradingdata['currentpos'] == -1:
            side = "Buy"
        if __tradingdata['currentpos'] == 1:            
            side = "Sell"
        print('New Position: ' + side)
        Trade_Logger.log_trade(side)
        if realTrading is True:
            API_Manager.create_order(side)     




    