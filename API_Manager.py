import ccxt
from threading import Thread, Event

import Candle_Manager

__exchange = None
__thread = None

def set_newexchange(name, APIkey, secret):
    global __exchange
    exchange_class = getattr(ccxt, name)
    __exchange = exchange_class({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_SECRET',
    'timeout': 30000,
    'enableRateLimit': True,
})

def get_Klines(symbol,timeframe = '1m', since = None, limit=750):
    if since is None:
        since = __exchange.milliseconds() - limit * 60 * 1000
    candles = __exchange.fetch_ohlcv(symbol, timeframe, since, limit)
    return candles

def open_klinesstream(symbol, interval='1m'):
    global __thread
    __thread = PriceStreamThread(Event(), 2, __exchange, Candle_Manager, symbol)
    __thread.start()

def close_klinestream():
    __thread.stopThread()

def create_order(side):
    __exchange.create_order("BTCUSD", "Market", side, 0.0001)  

class PriceStreamThread(Thread):
    def __init__(self, event, time, exchange, candlemanager, symbol):
        Thread.__init__(self)
        self.stopped = event
        self.exchange = exchange
        self.candleManager = candlemanager
        self.time = time
        self.symbol = symbol
        print('Started new pricestream thread for {}'.format(symbol))

    def run(self):
        while not self.stopped.wait(self.time):
            since = self.exchange.milliseconds() - 3 * 60 * 1000
            candles = self.exchange.fetch_ohlcv(self.symbol, '1m', since, 3)
            time = candles[0][0]
            if hasattr(self, 'lasttime'):
                if self.lasttime != time:
                    print("New Candle", candles)
                    self.candleManager.on_newcandle(candles[0])
            self.lasttime = time

    def stopThread(self):
        self.stopped.set()
        



    

