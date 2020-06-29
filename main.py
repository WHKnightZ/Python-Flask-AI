from app import create_app

from setting import ProdConfig

app = create_app(ProdConfig)

if __name__ == "__main__":
    app.run(port=5012, debug=True)
