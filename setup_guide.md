# Ballistics Web App — Full Setup Guide (Markdown)

## System Requirements:
- 2 GB+ RAM VPS or local machine
- Docker 20.x or higher
- Docker Compose 1.29+

## Deployment Process:

### 1. Preparation
- Unpack the ZIP file.
- Configure `.env` file with PostgreSQL, Stripe keys.

### 2. SSL Configuration
- Place `key.pem` and `cert.pem` in `./ssl` directory.

### 3. Build and Deploy Using Docker Compose
```
docker-compose up --build
```

### 4. Initialize Database
Run migrations inside the app container:
```
docker-compose exec app flask db init
docker-compose exec app flask db migrate -m "Initial migration"
docker-compose exec app flask db upgrade
```

### 5. Access the System
- Open browser: https://your-server/
- Login or create admin user using CLI or seeded user setup.

### Notes
- PostgreSQL is required.
- No SQLite fallback.
- Use Flask CLI commands for admin tasks.