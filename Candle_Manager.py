import APIs._Binance_API
from classes import Candle
import _thread as thread
import Candle_Manager
import InstanceHolder
import API_Manager
import queue

__currentCandles = []

def load_candles(symbol, interval='1m'):
    global __currentCandles
    candles = API_Manager.get_Klines(symbol,interval)
    if(candles != None):
        __currentCandles.clear() 
        for candle in reversed(candles):
            __currentCandles.append(Candle(candle[0],candle[1],candle[2],candle[3],candle[4],candle[5]))
        print('Loaded {} candles'.format(len(candles)))
    else:
        print('Symbol was not found')

def print_candles():
    for candle in __currentCandles:
        candle.printCandle()

def get_candles(length=len(__currentCandles)):
    return __currentCandles[:length]

def initiate_pricestream(symbol, interval='1m'):
    thread.start_new_thread(APIs._Binance_API.open_klinesstream, (symbol.lower(), interval))

def close_pricestream():
    API_Manager.close_klinestream()

def on_newcandle(candle):
    global __currentCandles
    newcandle = Candle(candle[0],candle[1],candle[2],candle[3],candle[4],candle[5])
    mainWindow = InstanceHolder.get_instance('MainWindow')
    __currentCandles.insert(0,newcandle)  
    if len(__currentCandles) > 1000:
        del __currentCandles[-1]
    mainWindow.add_queueitem('new_candle')
