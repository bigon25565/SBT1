from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def home():
    response = Response("1147329")
    response.headers["X-Author"] = "1147329"
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response
