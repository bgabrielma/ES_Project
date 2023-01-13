import os
import json

from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask("news")

@app.route("/", methods=['GET'])
def hello_world():
    return json.dumps({'name': 'alice',
                       'email': 'alice@outlook.com'})

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
