import requests
import json
import datetime

from flask import Flask, jsonify
from dotenv import load_dotenv

from utils import get_data

from constants import FULL_DAY_MILLISECONDS

load_dotenv()

app = Flask("coins")

@app.route("/coins/<string:type>/<int:days>", methods=['GET'])
def get_coins(type, days):
    """
    Args: 
    type = type of crypto coin
    days = int number of days. Maximum 14
    """
    data = get_data(type, days)
    
    return jsonify({
        "from": datetime.datetime.now().timestamp() - ((14 if days > 14 else days) * FULL_DAY_MILLISECONDS),
        "to": datetime.datetime.now().timestamp(),
        "coin": type,
        "data" : data
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
