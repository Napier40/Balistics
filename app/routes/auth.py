from flask import Blueprint, render_template, redirect, url_for, flash
from app import db
from app.models import User
from app.forms import RegistrationForm, LoginForm
from argon2 import PasswordHasher

auth_bp = Blueprint('auth', __name__)
ph = PasswordHasher()

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = ph.hash(form.password.data)
        user = User(username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', title='Register', form=form)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and ph.verify(user.password, form.password.data):
            # In a real app, you would use a login manager to handle the session
            flash('You have been logged in!', 'success')
            return redirect(url_for('user_dashboard.dashboard'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)