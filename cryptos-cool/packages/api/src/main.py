import os
import requests

from flask import Flask, request as flask_request, redirect, make_response
from dotenv import load_dotenv

load_dotenv()

app = Flask("API Gateway")

def build_query_params(url: str, query_string:str):
    return f"{url}" + (f"?{query_string}" if query_string else "")

@app.route("/api/news", methods=['GET'])
def forward_to_news_service():
    try:
        return requests.get(
            build_query_params(os.getenv("NEWS_API_PRIVATE_CONTAINER_URL"), flask_request.query_string.decode())
        ).json()
    except Exception as e:
        return {"error": str(e)}, 500

@app.route("/api/coins", methods=['GET'])
def forward_to_coins_service():
    try:
        type = flask_request.args.get("type")
        days = flask_request.args.get("days")

        if not type or not days:
            raise ValueError("Type or days field values are missing")

        url = os.getenv("COINS_API_PRIVATE_CONTAINER_URL")
        print(f"{url}/{type}/{days}")

        return requests.get(f"{url}/{type}/{days}").json()
    except Exception as e:
        return {"error": str(e)}, 500        

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
