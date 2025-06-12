from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def root():
    response = Response("1147329")
    response.headers["X-Author"] = "1147329"
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

@app.route("/login/")
def login():
    response = Response("1147329")
    response.headers["Content-Type"] = "text/plain; charset=UTF-8"
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

@app.route("/sample/")
def sample():
    code = """
function task(x) {
    return x * this * this;
}
""".strip()
    response = Response(code)
    response.headers["Content-Type"] = "text/plain; charset=UTF-8"
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response
