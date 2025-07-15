# Ballistics Web App PostgreSQL Deployment — Quick Reference

## Prerequisites:
- Python 3.12 or higher
- PostgreSQL

## Deployment Steps:
1️⃣ Unzip the deployment package.
2️⃣ Rename `.env.example` to `.env` and set your real secrets. Make sure to update the `DATABASE_URL` with your local database credentials.
3️⃣ Install the dependencies:
```
pip install -r requirements.txt
```
4️⃣ Run the database migrations:
```
export FLASK_APP=run.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```
5️⃣ Create the admin user:
```
export FLASK_APP=run.py
flask create-admin
```
6️⃣ Run the application:
```
python run.py
```

## Admin Access:
- Open http://localhost:5000/
- Login with the admin user:
    - **Username:** TestJohn
    - **Password:** Johnston