import datetime
import json
import requests

def build_url(type, endtime):
    # 1 day = 86,400 seconds
    current_time = datetime.datetime.now().timestamp()

    if endtime <= 7:
        endtime = current_time - (endtime * 86400)
        response = endpoint_builder(type, current_time, endtime)
        response = response.json()
    else:
        firstWeek =  endpoint_builder(type, current_time, current_time + (endtime * 86400))
        firstWeek = firstWeek.json()
        endtime = endtime - 7
        newTime = current_time - (7 * 86400)
        endtime = current_time - (endtime * 86400)
        secondWeek = endpoint_builder(type, newTime, endtime)
        secondWeek = secondWeek.json()

    return firstWeek
    # https://api.binance.com/api/v3/uiKlines

def endpoint_builder(type, current_time, endtime):
    
    endtime = int(endtime) * 1000
    current_time = int(current_time) * 1000
    api = f"https://api.binance.com/api/v3/uiKlines?symbol={type}EUR&interval=1m&endTime={endtime}&startTime={current_time}"
    print(api)
    return requests.get(f"https://api.binance.com/api/v3/uiKlines?symbol={type}EUR&interval=1m&endTime={endtime}&startTime={current_time}")

print(build_url("BTC",14))