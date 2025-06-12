from flask import Flask, request, Response
from PIL import Image
import io

app = Flask(__name__)

@app.route("/login")
def login():
    return Response("1147329", content_type="text/plain; charset=UTF-8")

@app.route("/makeimage")
def makeimage():
    width = request.args.get("width")
    height = request.args.get("height")

    try:
        width = int(width)
        height = int(height)
        if width <= 0 or height <= 0:
            raise ValueError
    except (TypeError, ValueError):
        return Response("Invalid width or height", status=400, content_type="text/plain; charset=UTF-8")

    img = Image.new("RGB", (width, height), color=(255, 255, 255))

    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    return Response(img_bytes.read(), content_type="image/png")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
