import requests

from flask import Flask, request as flask_request
from dotenv import load_dotenv
from utils import build_url

load_dotenv()

app = Flask("news")

@app.route("/news", methods=['GET'])
def get_news():
    """
    Args: 
        search -> Ex: crypto AND bitcoin
        page -> Ex: 1
        from -> Ex> 2023-01-01. Must be in YYYY-MM-DD
        to -> Ex> 2023-01-01. Must be in YYYY-MM-DD
    """
    url = build_url(flask_request.args)
    print(url)
    return requests.get(url).json()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
