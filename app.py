from flask import Flask, Response, jsonify, abort
from datetime import datetime
import re

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

# Новый маршрут /DDMMYY — формат даты текущей даты
@app.route("/<date_str>")
def date_route(date_str):
    # Проверяем, что строка из 6 цифр
    if not re.fullmatch(r"\d{6}", date_str):
        abort(404)

    # Получаем текущую дату
    now = datetime.now()

    # Форматируем дату в DDMMYY и сравниваем с date_str
    expected = now.strftime("%d%m%y")
    if date_str != expected:
        abort(404)

    # Форматируем дату в DD-MM-YYYY
    formatted_date = now.strftime("%d-%m-%Y")

    data = {
        "date": formatted_date,
        "login": "1147329"
    }
    return jsonify(data)

# Маршрут /api/rv/<abc> — переворачиваем строку abc, где abc — строчные латинские буквы
@app.route("/api/rv/<abc>")
def reverse_route(abc):
    if not re.fullmatch(r"[a-z]+", abc):
        abort(404)
    reversed_str = abc[::-1]
    return Response(reversed_str, content_type="text/plain; charset=UTF-8")
