import Candle_Manager
import datetime
__path = "/home/manuel/projects/CryptoPrinter/log.txt"
__lastprice = 0
__lastcandle = None

__resprofit = 0

def log_trade(side):
    global __lastprice
    global __lastcandle
    global __resprofit
    currentcandle = Candle_Manager.get_candles(1)[0]
    file = open(__path, "a")
    if __lastprice != 0: 
        dif = currentcandle.close - __lastprice
        precentage = (dif / currentcandle.close) * 100
        if side is "Buy":
            precentage *= -1
        __resprofit += precentage
        deltatime = (currentcandle.closetime - __lastcandle.closetime) / 60
        file.write("Closed position | Profit: {} in {} mins @ {} -> Total Profit: {}".format(round(precentage,3),
                                                                                    deltatime,
                                                                                    datetime.datetime.now().time(), 
                                                                                    __resprofit) + "\n")
    __lastcandle = currentcandle
    __lastprice = currentcandle.close
    file.write("New position: " + side + "\n")
    file.close()

def clear_log():
    open(__path, 'w').close()