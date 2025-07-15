from flask import Blueprint, render_template
from app import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def landing():
    return render_template('landing.html')

@main_bp.route('/db_test')
def db_test():
    try:
        db.session.query("1").all()
        return '<h1>Database connection successful!</h1>'
    except Exception as e:
        return f'<h1>Database connection failed: {e}</h1>'
