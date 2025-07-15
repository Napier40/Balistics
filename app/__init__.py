from flask import Flask
from .routes.ballistics import ballistics_bp
from .routes.user_dashboard import user_dashboard_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(ballistics_bp)
    app.register_blueprint(user_dashboard_bp)
    return app