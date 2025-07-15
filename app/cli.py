import click
from flask.cli import with_appcontext
from . import db
from .models import User
from argon2 import PasswordHasher

@click.command('create-admin')
@with_appcontext
def create_admin_command():
    """Creates the admin user."""
    ph = PasswordHasher()
    if not User.query.filter_by(username='TestJohn').first():
        hashed_password = ph.hash('Johnston')
        admin_user = User(username='TestJohn', password=hashed_password)
        db.session.add(admin_user)
        db.session.commit()
        click.echo('Admin user created successfully.')
    else:
        click.echo('Admin user already exists.')
