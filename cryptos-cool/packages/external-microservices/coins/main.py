import requests

from flask import Flask, request as flask_request
from dotenv import load_dotenv
from utils import build_url

load_dotenv()

app = Flask("coins")

@app.route("/coins/<string:type><int:endtime>", methods=['GET'])
def get_coins(type, endtime):
    """
    Args: 
    type = type of crypto coin
    endtime = int number of days
    """
    url = build_url(flask_request.args, type, endtime)
    return requests.get(url).json()

if __name__ == "__main__":
    app.run(host="localhost", port=1000, debug=True)
