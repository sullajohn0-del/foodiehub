# 🚀 Quick Deployment Guide - FoodieHub

## ⚡ Fastest Way: Render (Free & Easy)

### Step 1: Prepare Your Code

1. **Create a GitHub repository** and push your code:
   ```powershell
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/foodiehub.git
   git push -u origin main
   ```

2. **Make sure you have these files:**
   - ✅ `requirements.txt` (already created)
   - ✅ `Procfile` (already created)
   - ✅ `Dockerfile` (optional, already created)

### Step 2: Deploy to Render

1. **Go to https://render.com** and sign up (free)

2. **Create PostgreSQL Database:**
   - Click "New +" → "PostgreSQL"
   - Name: `foodiehub-db`
   - Plan: Free
   - Click "Create Database"
   - **Copy the Internal Database URL** (you'll need this)

3. **Create Web Service:**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Settings:
     - **Name:** `foodiehub`
     - **Region:** Choose closest to you
     - **Branch:** `main`
     - **Root Directory:** (leave empty)
     - **Runtime:** `Python 3`
     - **Build Command:** 
       ```
       pip install -r requirements.txt && python manage.py collectstatic --noinput
       ```
     - **Start Command:**
       ```
       gunicorn myproject.wsgi:application
       ```
     - **Plan:** Free

4. **Add Environment Variables:**
   Click "Environment" tab and add:
   ```
   DEBUG=False
   SECRET_KEY=your-random-secret-key-here-make-it-long-and-random
   DB_NAME=your-db-name-from-render
   DB_USER=your-db-user-from-render
   DB_PASSWORD=your-db-password-from-render
   DB_HOST=your-db-host-from-render
   DB_PORT=5432
   ALLOWED_HOSTS=your-app-name.onrender.com
   ```

5. **Deploy!**
   - Click "Create Web Service"
   - Wait for deployment (5-10 minutes)
   - Your app will be live at: `https://your-app-name.onrender.com`

### Step 3: Run Migrations

After deployment, go to Render dashboard:
- Click on your web service
- Go to "Shell" tab
- Run:
  ```bash
  python manage.py migrate
  python manage.py createsuperuser
  python manage.py populate_data
  ```

## 🎯 Alternative: Railway (Also Free)

1. **Go to https://railway.app** and sign up

2. **New Project** → "Deploy from GitHub repo"

3. **Add PostgreSQL:**
   - Click "+ New" → "Database" → "PostgreSQL"

4. **Set Environment Variables:**
   - `DEBUG=False`
   - `SECRET_KEY=your-secret-key`
   - `ALLOWED_HOSTS=your-app-name.railway.app`

5. **Deploy!** Railway auto-detects Django and deploys

## 📝 Before Deploying - Update Settings

Update `myproject/settings.py` to use environment variables:

```python
import os

# At the top, add:
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-os($-z@$fmg!25nfq6&dslljh8=_uhkv-)o*po$=gae*&8tpus')
DEBUG = os.environ.get('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',') if os.environ.get('ALLOWED_HOSTS') else []

# Update database section:
if os.environ.get('DB_NAME'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DB_NAME'),
            'USER': os.environ.get('DB_USER'),
            'PASSWORD': os.environ.get('DB_PASSWORD'),
            'HOST': os.environ.get('DB_HOST'),
            'PORT': os.environ.get('DB_PORT', '5432'),
        }
    }
```

## ✅ Post-Deployment Checklist

- [ ] Run migrations: `python manage.py migrate`
- [ ] Create superuser: `python manage.py createsuperuser`
- [ ] Populate data: `python manage.py populate_data`
- [ ] Test the website
- [ ] Set up custom domain (optional)
- [ ] Configure SSL/HTTPS (usually automatic)

## 🆘 Common Issues

**Static files not loading?**
- Make sure `collectstatic` runs in build command
- Check `STATIC_ROOT` setting

**Database errors?**
- Verify database credentials in environment variables
- Check database is running

**500 errors?**
- Check logs in Render/Railway dashboard
- Verify `ALLOWED_HOSTS` includes your domain
- Make sure `DEBUG=False` in production

---

**That's it!** Your FoodieHub app should be live in about 10 minutes! 🎉

