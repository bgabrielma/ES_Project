import os

import urllib.parse
from datetime import datetime

api_key = os.getenv("NEWS_API")
DEFAULT_PAGE_SIZE = 10

def build_url(args: dict):
    search = urllib.parse.quote(f'crypto AND {args.get("search", "crypto")}')
    page = args.get("page", 1)
    from_date = args.get("from", datetime.today().strftime('%Y-%m-%d'))
    to_date = args.get("to", datetime.today().strftime('%Y-%m-%d'))
    
    return f"https://newsapi.org/v2/everything?q={search}&searchIn=title,description&pageSize={DEFAULT_PAGE_SIZE}&page={page}&apiKey={api_key}&from={from_date}&to={to_date}"