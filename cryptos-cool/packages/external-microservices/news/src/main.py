import requests

from flask import Flask, request as flask_request, jsonify
from dotenv import load_dotenv
from utils import build_url, get_api_keys, filter_news_by_date, DEFAULT_PAGE_SIZE
from datetime import datetime, timedelta

load_dotenv()

app = Flask("news")
api_keys: list[str] = get_api_keys()

def fetch_data(args):
    for api_key in api_keys:
        # Fill api_key value with current api value
        url = build_url(args, api_key)
        data:dict =  requests.get(url).json()

        if(data.get("code") != "rateLimited"):
            from_date = datetime.strptime(args.get("from_date", (datetime.today() - timedelta(weeks=12)).strftime('%Y-%m-%d')), '%Y-%m-%d')
            return filter_news_by_date(data, from_date)

    return jsonify({"error": "rateLimited"})

@app.route("/news", methods=['GET'])
def get_news():
    """
    Args: 
        search -> Ex: crypto AND bitcoin
        page -> Ex: 1
        from_date -> Ex> 2023-01-01. Must be in YYYY-MM-DD
    """

    data:dict = fetch_data(flask_request.args)

    articles = data.get("articles", [])
    total_results = len(articles)
    total_pages = round(float(total_results / DEFAULT_PAGE_SIZE))

    return jsonify({
        "articles": data.get("articles", []),
        "pages": total_pages,
        "total_results": 100 if total_results > 100 else total_results
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
