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

def create_admin_user():
    from app.models import User
    from argon2 import PasswordHasher
    ph = PasswordHasher()

    with create_app().app_context():
        if not User.query.filter_by(username='TestJohn').first():
            hashed_password = ph.hash('Johnston')
            admin_user = User(username='TestJohn', password=hashed_password)
            db.session.add(admin_user)
            db.session.commit()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    with app.app_context():
        db.create_all()
        create_admin_user()

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