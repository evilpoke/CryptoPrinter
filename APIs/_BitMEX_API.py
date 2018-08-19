import requests
import json
import time
import hmac
import hashlib
import json
from urllib.parse import urlparse

__baseURL = "https://testnet.bitmex.com/api/v1"
__signatureURL = "/api/v1"
__endpoints = {'newpos': '/order'}

__apiKey = ""
__apiSecret = ""

def __post_data(endpoint, d, printResult=False):
    data = str(d)
    finalstring = ''
    for char in data:
        if char == "'":
            finalstring += '"'
        elif char != ' ':
            finalstring += char
        
    h = __get_header("POST",endpoint,finalstring)
    response = requests.post(__baseURL + __endpoints[endpoint], headers=h, data=d)
    print(response.content)

def __get_header(verb, endpoint, data):
    h = {}
    expireTime = int(round(time.time())+5)
    h['api-expires'] = str(expireTime)
    h['api-key'] = __apiKey
    h['api-signature'] = __generate_signature(verb, __signatureURL + __endpoints[endpoint], expireTime, data)
    return h

def __generate_signature(verb, url, expires, data):
    message = verb + url + str(expires) + data
    print(message)

    signature = hmac.new(bytes(__apiSecret, 'utf8'), bytes(message, 'utf8'), digestmod=hashlib.sha256).hexdigest()
    return signature

def set_newpos(symbol, side, quantity):
    d = {}
    d["symbol"] = symbol
    d["side"] = side
    d["simpleOrderQty"] = quantity
    d["orderType"] = "Market"
    __post_data('newpos', d)

if __name__ == '__main__':  
    set_newpos("XBT-USD", "Sell", 0.0001)
    
    



    

