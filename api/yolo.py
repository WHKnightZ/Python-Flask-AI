from flask import Blueprint, request
from YOLO.yolo import predict_image

api = Blueprint("yolo", __name__)


@api.route('', methods=['POST'])
def predict():
    data = request.get_json()
    data = data.get("image", None)
    data = predict_image(data)
    return {"predict": data.decode()}
