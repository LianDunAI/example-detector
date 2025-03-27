from flask import Flask
from flask import request, Response
import json
from detect import RandomDetector

app = Flask(__name__)
detector = RandomDetector()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/detect", methods=['POST'])
def detect():
    try:
        cap_image_path = request.json['cap_image_path']
        ref_image_path = request.json['ref_image_path']
        result = detector.detect(cap_image_path, ref_image_path)
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
