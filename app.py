from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET,POST,PUT,DELETE,OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "x-test,ngrok-skip-browser-warning,Content-Type,Accept,Access-Control-Allow-Headers"
    return response

@app.after_request
def apply_cors(response):
    return add_cors_headers(response)

@app.route("/result4/", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
def result4():
    if request.method == "OPTIONS":
        response = make_response("", 204)
        return add_cors_headers(response)

    x_test = request.headers.get("x-test", "")

    try:
        x_body = request.get_data(as_text=True)
    except Exception:
        x_body = ""

    data = {
        "message": "1147329",
        "x-result": x_test,
        "x-body": x_body
    }
    response = jsonify(data)
    response.headers["Content-Type"] = "application/json"
    return response
