from flask import Flask, Response

app = Flask(__name__)

def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

@app.after_request
def apply_cors(response):
    return add_cors_headers(response)

@app.route("/")
def root():
    response = Response("1147329")
    response.headers["X-Author"] = "1147329"
    return response

@app.route("/login/")
def login():
    return Response("1147329", content_type="text/plain; charset=UTF-8")

@app.route("/promise/")
def promise():
    code = """
function task(x) {
    return new Promise((resolve, reject) => {
        if (x < 18) {
            resolve("yes");
        } else {
            reject("no");
        }
    });
}
""".strip()
    return Response(code, content_type="text/plain; charset=UTF-8")

@app.route("/fetch/")
def fetch():
    html = """
<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"></head>
<body>
    <input id="inp" type="text">
    <button id="bt">Fetch</button>
    <script>
        document.getElementById("bt").addEventListener("click", async () => {
            const input = document.getElementById("inp");
            try {
                const res = await fetch(input.value);
                const text = await res.text();
                input.value = text;
            } catch (e) {
                input.value = "ERROR";
            }
        });
    </script>
</body>
</html>
""".strip()
    return Response(html, content_type="text/html; charset=UTF-8")
