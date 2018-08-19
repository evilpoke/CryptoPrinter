import Candle_Manager
import Indicator_Manager
import Trade_Logger

import numpy as np
import ccxt

__trailingvalue = {'trailing': False, 'trailvalue': 5, 'lasttrail': 0}

__tradingdata = {'lastpos': 0, 'currentpos': 0}

__currentexchange = None

realTrading = False

def startTrading(symbol, interval):
    Candle_Manager.load_candles(symbol, interval=interval)
    Candle_Manager.initiate_pricestream(symbol, interval=interval)  

def instantiate_newexchange(exchangename, key, secret):
    exchange_class = getattr(ccxt, exchangename)
    __currentexchange = exchange_class({
        'apiKey': 'key',
        'secret': 'secret',
        'timeout': 30000,
        'enableRateLimit': True,
    })
    __currentexchange.load_markets()
    
def on_newprice():
    __check_indicatordata()

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
            __currentexchange.create_order("BTCUSD", "Market", side, 0.0001)       




    