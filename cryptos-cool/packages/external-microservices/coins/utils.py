import os

import requests


import urllib.parse
import datetime

api_key = os.getenv("COINS_API")
DEFAULT_PAGE_SIZE = 10

def build_url(args: dict, type, endtime):
    # 1 day = 86,400 seconds
    current_time = datetime.datetime.now().timestamp()

    if endtime <= 7:
        endtime = current_time - (endtime * 86400)
        response = endpoint_builder(type, current_time, endtime)
        response = response.json()
    else:
        firstWeek =  endpoint_builder(type, current_time)
        endtime = endtime - 7
        newTime = current_time - (7 * 86400)
        endtime = current_time - (endtime * 86400)
        secondWeek = endpoint_builder(type, newTime, endtime)
        secondWeek = secondWeek.json()

    return response
    # https://api.binance.com/api/v3/uiKlines

def endpoint_builder(type, current_time, endtime = 7):
    endtime = endtime * 1000
    current_time = current_time * 1000
    return requests.get("https://api.binance.com/api/v3/uiKlines?symbol={type}EUR&interval=1m&endTime={endtime}&startTime={current_time}")

def dict_structure(response):
    dict = {
        "from": response[0],
        "to":response[1]
        ""} 


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