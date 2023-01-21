import requests

from flask import Flask, request as flask_request, jsonify
from dotenv import load_dotenv
from utils import build_url, get_api_keys, DEFAULT_PAGE_SIZE

load_dotenv()

app = Flask("news")
api_keys: list[str] = get_api_keys()

def fetch_data(args):
    for api_key in api_keys:
        # Fill api_key value with current api value
        url = build_url(args, api_key)
        data:dict =  requests.get(url).json()

        if(data.get("code") != "rateLimited"):
            return data

    return jsonify({"error": "rateLimited"})

@app.route("/news", methods=['GET'])
def get_news():
    """
    Args: 
        search -> Ex: crypto AND bitcoin
        page -> Ex: 1
        from -> Ex> 2023-01-01. Must be in YYYY-MM-DD
        to -> Ex> 2023-01-01. Must be in YYYY-MM-DD
    """

    data:dict = fetch_data(flask_request.args)

    total_results = data.get("totalResults", 0)
    total_pages = int(100 / DEFAULT_PAGE_SIZE)

    return jsonify({
        "articles": data.get("articles", []),
        "pages": total_pages,
        "total_results": total_results
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
