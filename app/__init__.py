from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import quote_bp
    app.register_blueprint(quote_bp)

    return app
