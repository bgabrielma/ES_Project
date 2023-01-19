import datetime

import json
from collections import defaultdict
import requests

def build_url(type, endtime):
    # 1 day = 86,400 seconds
    current_time = datetime.datetime.now().timestamp()

    if endtime <= 7:
        endtime = current_time - (endtime * 86400)
        response = endpoint_builder(type, current_time, endtime)
        response = response.json()
        response = dict_structure(response)
    else:
        firstloop = current_time - (7 * 86400)
        print(firstloop)
        firstWeek =  endpoint_builder(type, current_time, firstloop)
        firstWeek = firstWeek.json()
        response = dict_structure(firstWeek)
        # ex:
        # 12-7 = 5 dias que faltam
        newendtime = endtime - 7
        # novo tempo onde vai começar a proxima pesquisa remove-se os 7 dias ja pesquisados
        newTime = current_time - (7 * 86400)
        # adicionar os 5 dias que faltam
        endtime = newTime - (newendtime * 86400)
        secondWeek = endpoint_builder(type, newTime, endtime )
        secondWeek = secondWeek.json()
        
        response = dict_structure(secondWeek, response)

    return response
    # https://api.binance.com/api/v3/uiKlines

def endpoint_builder(type, current_time, endtime):
    
    endtime = int(endtime) * 1000
    current_time = int(current_time) * 1000
    print(f"https://api.binance.com/api/v3/uiKlines?symbol={type}EUR&interval=1m&endTime={current_time}&startTime={endtime}")
    return requests.get(f"https://api.binance.com/api/v3/uiKlines?symbol={type}EUR&interval=1m&endTime={current_time}&startTime={endtime}")

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