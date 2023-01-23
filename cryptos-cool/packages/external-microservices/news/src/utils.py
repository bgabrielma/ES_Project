import os

import urllib.parse
from datetime import datetime, timedelta

DEFAULT_PAGE_SIZE = 10

def build_url(args: dict, api_key: str):
    search = urllib.parse.quote(f'crypto AND {args.get("search", "crypto")}')
    page = args.get("page", 1)
    from_date = args.get("from", datetime.today().strftime('%Y-%m-%d'))
    to_date = args.get("to", (datetime.today() - timedelta(weeks=12)).strftime('%Y-%m-%d'))
    
    return f"https://newsapi.org/v2/everything?q={search}&searchIn=title,description&pageSize={DEFAULT_PAGE_SIZE}&page={page}&apiKey={api_key}&from={from_date}&to={to_date}"

def get_api_keys():
    api_key_1 = os.getenv("NEWS_API_1")
    api_key_2 = os.getenv("NEWS_API_2")
    api_key_3 = os.getenv("NEWS_API_3")
    api_key_4 = os.getenv("NEWS_API_4")
    return [api_key_1, api_key_2, api_key_3, api_key_4]