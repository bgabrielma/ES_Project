import datetime
import json
import requests

from collections import defaultdict
from constants import FULL_DAY_SECONDS

def get_data(type, days = 7):
    # 1 day = 86,400 seconds
    current_time = datetime.datetime.now().timestamp()

    if days <= 7:
        end_time = current_time - (days * FULL_DAY_SECONDS)
        response = endpoint_builder(type, current_time, end_time)
       
        response = dict_structure(response)
    else:
        first_week_dataSet = endpoint_builder(type, current_time, current_time - (7 * FULL_DAY_SECONDS))
 
        # if days are above 14 it regulates

        # ex:
        # 12-7 = 5 days left
        remaing_days = (14 if days > 14 else days) - 7
        # new time where whe are going to start the new search after removing the 7 days
        new_time = current_time - (7 * FULL_DAY_SECONDS)
        # add the 5 missing days
        end_time = new_time - (remaing_days * FULL_DAY_SECONDS)
        second_week_dataset = endpoint_builder(type, new_time, end_time)
        
        
    return dict_structure(first_week_dataSet,second_week_dataset)
    # https://api.binance.com/api/v3/uiKlines

def endpoint_builder(type, current_time, end_time):
    end_time = int(end_time) * 1000
    current_time = int(current_time) * 1000

    return requests.get(f"https://api.binance.com/api/v3/uiKlines?symbol={type}EUR&interval=1m&endTime={current_time}&startTime={end_time}").json()

def dict_structure(*response):
    # array de datas
    # array de prices
    data_dataset=[]
    price_dataset=[]
    for i in range(0,len(response)):
        for k in range(0, len(response[i])):

            # array de datas
                # + add From
                # + add To
            # array de prices
                # + add Open
                # + add Close

            # Insert information of open coin price information from the candle
            data_dataset.append(response[i][k][0])
            price_dataset.append(response[i][k][1])

            # Insert information of close coin price information from the candle
            data_dataset.append(response[i][k][6])
            price_dataset.append(response[i][k][3])

    return [price_dataset, data_dataset]

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