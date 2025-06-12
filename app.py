from flask import Flask, request, jsonify, Response
from PIL import Image
import io

app = Flask(__name__)

@app.route("/login", methods=["GET"])
def login():
    return Response("1147329", content_type="text/plain; charset=UTF-8")

@app.route("/size2json", methods=["POST"])
def size2json():
    if "image" not in request.files:
        return jsonify({"error": "No image part"}), 400
    
    file = request.files["image"]

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    try:
        img_bytes = file.read()
        img = Image.open(io.BytesIO(img_bytes))

        if img.format != "PNG":
            return jsonify({"error": "File is not PNG"}), 400

        width, height = img.size
        return jsonify({"width": width, "height": height})

    except Exception:
        return jsonify({"error": "Invalid image"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
