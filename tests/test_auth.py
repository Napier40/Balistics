import unittest
from app import create_app, db
from app.models import User
from argon2 import PasswordHasher

class AuthTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_register(self):
        response = self.client.post('/register', data={
            'username': 'testuser',
            'password': 'password',
            'confirm_password': 'password'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Your account has been created!', response.data)

    def test_login_logout(self):
        # Register a new user
        ph = PasswordHasher()
        hashed_password = ph.hash('password')
        user = User(username='testuser', password=hashed_password)
        with self.app.app_context():
            db.session.add(user)
            db.session.commit()

        # Log in
        response = self.client.post('/login', data={
            'username': 'testuser',
            'password': 'password'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Dashboard', response.data)

        # Log out
        response = self.client.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Ballistics App', response.data)

if __name__ == '__main__':
    unittest.main()
