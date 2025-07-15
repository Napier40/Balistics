import os
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
calibers = []

def load_calibers():
    global calibers
    with open('calibers.json') as f:
        calibers = json.load(f)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    load_calibers()

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .routes.main import main_bp
    from .routes.ballistics import ballistics_bp
    from .routes.user_dashboard import user_dashboard_bp
    from .routes.auth import auth_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(ballistics_bp)
    app.register_blueprint(user_dashboard_bp)
    app.register_blueprint(auth_bp)

    return app