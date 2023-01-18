import os
import time
import requests


import urllib.parse
from datetime import datetime

api_key = os.getenv("COINS_API")
DEFAULT_PAGE_SIZE = 10

def build_url(args: dict, type, endtime):
    # 1 day = 86,400 seconds
    current_time = datetime.datetime.now()
    if endtime <= 7:
        endtime = current_time - (endtime * 86400)
        response = endpoint_builder(type, endtime, current_time)
        response = response.json()
    else:
        endtime = endtime - 7
        response = endpoint_builder(type, endtime, current_time)
        response = response.json()

    return response
    # https://api.binance.com/api/v3/uiKlines
    
def endpoint_builder(type, endtime, current_time):
    return requests.get("https://api.binance.com/api/v3/uiKlines?symbol={type}EUR&interval=1m&endTime={endtime}&startTime={current_time}")