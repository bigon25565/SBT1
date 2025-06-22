from flask import Flask, request, send_file, jsonify
from PIL import Image
import io

app = Flask(__name__)

@app.route('/makeimage', methods=['GET'])
def makeimage():
    try:
        width = int(request.args.get('width'))
        height = int(request.args.get('height'))
    except (TypeError, ValueError):
        return "Invalid width or height", 400

    if width <= 0 or height <= 0 or width > 2000 or height > 2000:
        return "Invalid image size", 400

    image = Image.new("RGB", (width, height), "red")

    img_io = io.BytesIO()
    image.save(img_io, format='PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')

@app.route('/login')
def login():
    return '1147329'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
