import datetime

import json
from collections import defaultdict
import requests

def build_url(type, endTime = 7):
    # 1 day = 86,400 seconds
    currentTime = datetime.datetime.now().timestamp()

    if endTime <= 7:
        endTime = currentTime - (endTime * 86400)
        response = endpoint_builder(type, currentTime, endTime)
       
        response = dict_structure(response)
    else:
        firstloop = currentTime - (7 * 86400)
        firstWeek =  endpoint_builder(type, currentTime, firstloop)
    
        response = dict_structure(firstWeek)
        # ex:
        # 12-7 = 5 dias que faltam
        newendTime = endTime - 7
        # novo tempo onde vai começar a proxima pesquisa remove-se os 7 dias ja pesquisados
        newTime = currentTime - (7 * 86400)
        # adicionar os 5 dias que faltam
        endTime = newTime - (newendTime * 86400)
        secondWeek = endpoint_builder(type, newTime, endTime )
       
        
        response = dict_structure(secondWeek, response)

    return response
    # https://api.binance.com/api/v3/uiKlines

def endpoint_builder(type, currentTime, endTime):
    
    endTime = int(endTime) * 1000
    currentTime = int(currentTime) * 1000
    return requests.get(f"https://api.binance.com/api/v3/uiKlines?symbol={type}EUR&interval=1m&endTime={currentTime}&startTime={endTime}").json()

def dict_structure(response, dict_sub = defaultdict(list)):
    for k in range(0, len(response[0])):
        dict_sub["From"].append(response[k][0])
        dict_sub["To"].append(response[k][6])
        dict_sub["Open"].append(response[k][1])
        dict_sub["High"].append(response[k][2])
        dict_sub["Close"].append(response[k][3])
  
    return dict_sub

    #  1499040000000,      // Kline open time
    # "0.01634790",       // Open price
    # "0.80000000",       // High price
    # "0.01575800",       // Low price
    # "0.01577100",       // Close price
    # "148976.11427815",  // Volume
    # 1499644799999,      // Kline close time
    # "2434.19055334",    // Quote asset volume
    # 308,                // Number of trades
    # "1756.87402397",    // Taker buy base asset volume
    # "28.46694368",      // Taker buy quote asset volume
    # "0"                 // Unused field. Ignore.