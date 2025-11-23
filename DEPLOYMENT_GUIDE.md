# 🚀 FoodieHub Deployment Guide

This guide covers multiple deployment options for your Django FoodieHub application.

## 📋 Pre-Deployment Checklist

Before deploying, make sure to:

- [ ] Update `DEBUG = False` in settings
- [ ] Set `ALLOWED_HOSTS` with your domain
- [ ] Configure a production database (PostgreSQL recommended)
- [ ] Set up static files collection
- [ ] Configure environment variables for secrets
- [ ] Set up proper error logging
- [ ] Test the application thoroughly

## 🔧 Step 1: Prepare Your Django Settings

### Update `myproject/settings.py`

```python
import os
from pathlib import Path

# ... existing code ...

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com', 'localhost', '127.0.0.1']

# Database - Use PostgreSQL in production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'foodiehub'),
        'USER': os.environ.get('DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Security settings for production
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
```

### Create `requirements.txt`

```bash
cd C:\Users\sulla\OneDrive\Desktop\shop\myproject
C:\Users\sulla\OneDrive\Desktop\shop\myenv\Scripts\python.exe -m pip freeze > requirements.txt
```

Make sure it includes:
```
Django>=5.2.8
psycopg2-binary>=2.9.0
Pillow>=12.0.0
gunicorn>=21.2.0
whitenoise>=6.6.0
python-decouple>=3.8
```

## 🌐 Option 1: Deploy to Render (Recommended for Beginners)

Render is free and easy to use.

### Steps:

1. **Create a Render account** at https://render.com

2. **Create a PostgreSQL database:**
   - New → PostgreSQL
   - Name: `foodiehub-db`
   - Copy the Internal Database URL

3. **Create a Web Service:**
   - New → Web Service
   - Connect your GitHub repository
   - Settings:
     - **Build Command:** `pip install -r requirements.txt && python manage.py collectstatic --noinput`
     - **Start Command:** `gunicorn myproject.wsgi:application`
     - **Environment Variables:**
       ```
       DEBUG=False
       SECRET_KEY=your-secret-key-here
       DB_NAME=your-db-name
       DB_USER=your-db-user
       DB_PASSWORD=your-db-password
       DB_HOST=your-db-host
       DB_PORT=5432
       ```

4. **Deploy!**

## 🚂 Option 2: Deploy to Railway

Railway is another great free option.

### Steps:

1. **Create account** at https://railway.app

2. **Install Railway CLI:**
   ```powershell
   npm install -g @railway/cli
   ```

3. **Login:**
   ```powershell
   railway login
   ```

4. **Initialize project:**
   ```powershell
   cd C:\Users\sulla\OneDrive\Desktop\shop\myproject
   railway init
   ```

5. **Add PostgreSQL:**
   ```powershell
   railway add postgresql
   ```

6. **Set environment variables:**
   ```powershell
   railway variables set DEBUG=False
   railway variables set SECRET_KEY=your-secret-key
   ```

7. **Deploy:**
   ```powershell
   railway up
   ```

## 🐳 Option 3: Deploy with Docker

### Create `Dockerfile`

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Run gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]
```

### Create `docker-compose.yml`

```yaml
version: '3.8'

services:
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: foodiehub
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    volumes:
      - postgres_data:/var/lib/postgresql/data

  web:
    build: .
    command: gunicorn myproject.wsgi:application --bind 0.0.0.0:8000
    volumes:
      - .:/app
      - static_volume:/app/staticfiles
      - media_volume:/app/media
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      DEBUG: "False"
      DB_NAME: foodiehub
      DB_USER: postgres
      DB_PASSWORD: postgres
      DB_HOST: db
      DB_PORT: "5432"

volumes:
  postgres_data:
  static_volume:
  media_volume:
```

### Deploy to Docker Hub / Cloud:

```powershell
# Build
docker build -t foodiehub:latest .

# Run locally
docker-compose up

# Push to registry
docker tag foodiehub:latest yourusername/foodiehub:latest
docker push yourusername/foodiehub:latest
```

## ☁️ Option 4: Deploy to AWS (Advanced)

### Using AWS Elastic Beanstalk:

1. **Install EB CLI:**
   ```powershell
   pip install awsebcli
   ```

2. **Initialize:**
   ```powershell
   eb init
   ```

3. **Create environment:**
   ```powershell
   eb create foodiehub-env
   ```

4. **Deploy:**
   ```powershell
   eb deploy
   ```

## 🖥️ Option 5: Deploy to VPS (DigitalOcean, Linode, etc.)

### Steps:

1. **Set up Ubuntu server**

2. **Install dependencies:**
   ```bash
   sudo apt update
   sudo apt install python3-pip python3-venv postgresql nginx
   ```

3. **Clone your project:**
   ```bash
   git clone your-repo-url
   cd myproject
   ```

4. **Set up virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

5. **Set up PostgreSQL:**
   ```bash
   sudo -u postgres createdb foodiehub
   sudo -u postgres createuser foodiehub_user
   ```

6. **Run migrations:**
   ```bash
   python manage.py migrate
   python manage.py collectstatic
   ```

7. **Set up Gunicorn:**
   ```bash
   pip install gunicorn
   ```

8. **Create systemd service** (`/etc/systemd/system/foodiehub.service`):
   ```ini
   [Unit]
   Description=FoodieHub Gunicorn daemon
   After=network.target

   [Service]
   User=www-data
   Group=www-data
   WorkingDirectory=/path/to/myproject
   ExecStart=/path/to/venv/bin/gunicorn --workers 3 --bind unix:/path/to/myproject/foodiehub.sock myproject.wsgi:application

   [Install]
   WantedBy=multi-user.target
   ```

9. **Configure Nginx** (`/etc/nginx/sites-available/foodiehub`):
   ```nginx
   server {
       listen 80;
       server_name yourdomain.com;

       location /static/ {
           alias /path/to/myproject/staticfiles/;
       }

       location /media/ {
           alias /path/to/myproject/media/;
       }

       location / {
           proxy_pass http://unix:/path/to/myproject/foodiehub.sock;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

10. **Start services:**
    ```bash
    sudo systemctl start foodiehub
    sudo systemctl enable foodiehub
    sudo nginx -t
    sudo systemctl restart nginx
    ```

## 📝 Important Files to Create

### `.env` file (for local development)

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
DB_NAME=foodiehub
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432
```

### `.gitignore`

```
*.pyc
__pycache__/
*.log
.env
db.sqlite3
staticfiles/
media/
venv/
.venv/
```

### `Procfile` (for Heroku/Render)

```
web: gunicorn myproject.wsgi:application
release: python manage.py migrate
```

## 🔐 Security Checklist

- [ ] Change `SECRET_KEY` to a random string
- [ ] Set `DEBUG = False`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Use environment variables for sensitive data
- [ ] Enable HTTPS/SSL
- [ ] Set up proper database backups
- [ ] Configure CORS if needed
- [ ] Set up error monitoring (Sentry, etc.)

## 🧪 Testing Before Deployment

```powershell
# Run migrations
.\django.ps1 migrate

# Collect static files
.\django.ps1 collectstatic

# Test with production settings
set DJANGO_SETTINGS_MODULE=myproject.settings
.\django.ps1 check --deploy

# Run server with gunicorn (test)
pip install gunicorn
gunicorn myproject.wsgi:application
```

## 📚 Additional Resources

- Django Deployment Checklist: https://docs.djangoproject.com/en/stable/howto/deployment/checklist/
- Render Docs: https://render.com/docs
- Railway Docs: https://docs.railway.app
- DigitalOcean Django Tutorial: https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-20-04

## 🆘 Troubleshooting

**Issue: Static files not loading**
- Run: `python manage.py collectstatic`
- Check `STATIC_ROOT` and `STATIC_URL` settings
- Configure web server to serve static files

**Issue: Database connection errors**
- Check database credentials
- Ensure database is accessible
- Verify `DB_HOST` and `DB_PORT`

**Issue: 500 errors**
- Check `DEBUG = False` and set up proper logging
- Check server logs
- Verify `ALLOWED_HOSTS` includes your domain

---

**Need help?** Check Django documentation or your hosting provider's support.

