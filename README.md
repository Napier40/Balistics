# Ballistics Web App PostgreSQL Deployment — Quick Reference

## Prerequisites:
- Docker & Docker Compose installed
- PostgreSQL service will run as container
- SSL certificates for nginx in ./ssl/

## Deployment Steps:
1️⃣ Unzip the deployment package.
2️⃣ Rename `.env.example` to `.env` and set your real secrets.
3️⃣ Generate SSL certificates and place them in `ssl/` folder.

Example self-signed:
```
openssl req -x509 -newkey rsa:4096 -keyout ssl/key.pem -out ssl/cert.pem -days 365 -nodes
```

4️⃣ Build and start containers:
```
docker-compose up --build
```

5️⃣ Run PostgreSQL migrations:
```
docker-compose exec app flask db init
docker-compose exec app flask db migrate -m "Initial migration"
docker-compose exec app flask db upgrade
```

## Admin Access:
- Open https://your-server-address/
- Login with a pre-created admin user or create one using the Flask CLI.