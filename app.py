from flask import Flask
from flask import request, Response
import json
import base64
import numpy as np
from detect import RandomDetector

app = Flask(__name__)
detector = RandomDetector()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/detect", methods=['POST'])
def detect():
    try:
        cap_image = request.json['cap_image']
        ref_image = request.json['ref_image']
        image_is_path = request.json['image_is_path']
        if not image_is_path:
            cap_image = np.frombuffer(base64.b64decode(cap_image), dtype="uint8")
            ref_image = np.frombuffer(base64.b64decode(ref_image), dtype="uint8")
        result = detector.detect(cap_image, ref_image, image_is_path)
        response_data = result
        response_json = json.dumps(response_data)
        response_stat = 200
    except Exception as e:
        response_data = {"status": 500, "msg": f"{e}"}
        response_json = json.dumps(response_data)
        response_stat = 500
    return Response(response_json, status=response_stat, mimetype="application/json")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8088)
