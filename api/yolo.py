from flask import Blueprint, request
from YOLO.yolo import predict_image
import time

api = Blueprint("yolo", __name__)


@api.route('', methods=['POST'])
def predict():
    data = request.get_json()
    data = data.get("image", None)
    start = time.time()
    data = predict_image(data).decode("utf-8")
    print(time.time() - start)
    return {"predict": data}
