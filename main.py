from app import create_app
from flask_cors import CORS

from setting import ProdConfig

app = create_app(ProdConfig)
CORS(app)

if __name__ == "__main__":
    app.run(port=5012, debug=True)
