import os

import urllib.parse
from datetime import datetime, timedelta

DEFAULT_PAGE_SIZE = 10

def build_url(args: dict, api_key: str):
    search = urllib.parse.quote(args.get("search", "crypto"))
    page = args.get("page", 1)
    
    url = f"https://newsapi.org/v2/everything?q={search}&searchIn=title,description&pageSize=100&sortBy=publishedAt&apiKey={api_key}"
    return url

def get_api_keys():
    api_key_1 = os.getenv("NEWS_API_1")
    api_key_2 = os.getenv("NEWS_API_2")
    api_key_3 = os.getenv("NEWS_API_3")
    api_key_4 = os.getenv("NEWS_API_4")
    return [api_key_1, api_key_2, api_key_3, api_key_4]

def filter_news_by_date(data: dict, minimum_date: str):
    new_array_of_dict = []
    copied_dict = data.copy()

    print(minimum_date)

    for dict in copied_dict.get("articles"):
        publishedAt = dict.get("publishedAt", None)
        print(datetime.strptime(publishedAt, '%Y-%m-%dT%H:%M:%S%z').date() > minimum_date.date())
        if publishedAt is not None and datetime.strptime(publishedAt, '%Y-%m-%dT%H:%M:%S%z').date() >= minimum_date.date():
            new_array_of_dict.append(dict)

    copied_dict.update({ "articles": new_array_of_dict })         
    return copied_dict