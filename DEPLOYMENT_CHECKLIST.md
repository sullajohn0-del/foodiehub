# ✅ Deployment Checklist - FoodieHub

## Pre-Deployment Steps

### 1. ✅ Settings Updated
- [x] `settings.py` now uses environment variables
- [x] Database configuration supports PostgreSQL
- [x] Security settings added for production
- [x] Static files configured

### 2. Files Ready
- [x] `requirements.txt` - All dependencies listed
- [x] `Procfile` - For Render/Heroku
- [x] `Dockerfile` - For Docker deployments
- [x] `.gitignore` - Excludes unnecessary files

### 3. Before You Deploy

#### Generate a New Secret Key
```powershell
cd C:\Users\sulla\OneDrive\Desktop\shop\myproject
C:\Users\sulla\OneDrive\Desktop\shop\myenv\Scripts\python.exe -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

**Save this key!** You'll need it for production.

#### Test Locally First
```powershell
# Test with production-like settings
set DEBUG=False
set ALLOWED_HOSTS=localhost,127.0.0.1
.\django.ps1 runserver
```

## 🚀 Deployment Steps

### Option A: Render (Recommended)

1. **Push to GitHub:**
   ```powershell
   git init
   git add .
   git commit -m "FoodieHub - Ready for deployment"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/foodiehub.git
   git push -u origin main
   ```

2. **Create Render Account:**
   - Go to https://render.com
   - Sign up with GitHub

3. **Create PostgreSQL Database:**
   - New + → PostgreSQL
   - Name: `foodiehub-db`
   - Plan: Free
   - **Copy the Internal Database URL**

4. **Create Web Service:**
   - New + → Web Service
   - Connect GitHub repo
   - Settings:
     - **Name:** `foodiehub`
     - **Build Command:** `pip install -r requirements.txt && python manage.py collectstatic --noinput`
     - **Start Command:** `gunicorn myproject.wsgi:application`

5. **Set Environment Variables:**
   ```
   DEBUG=False
   SECRET_KEY=<your-generated-secret-key>
   DB_NAME=<from-render-database>
   DB_USER=<from-render-database>
   DB_PASSWORD=<from-render-database>
   DB_HOST=<from-render-database>
   DB_PORT=5432
   ALLOWED_HOSTS=your-app-name.onrender.com
   ```

6. **Deploy & Run Migrations:**
   - After deployment, go to Shell tab
   - Run:
     ```bash
     python manage.py migrate
     python manage.py createsuperuser
     python manage.py populate_data
     ```

### Option B: Railway

1. **Push to GitHub** (same as above)

2. **Go to Railway:**
   - https://railway.app
   - New Project → Deploy from GitHub

3. **Add PostgreSQL:**
   - + New → Database → PostgreSQL

4. **Set Environment Variables:**
   - `DEBUG=False`
   - `SECRET_KEY=<your-secret-key>`
   - `ALLOWED_HOSTS=your-app-name.railway.app`

5. **Deploy!** Railway auto-detects Django

## 🔐 Environment Variables Reference

### Required for Production:
```
DEBUG=False
SECRET_KEY=<generate-new-key>
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
```

### Database (PostgreSQL):
```
DB_NAME=foodiehub
DB_USER=postgres
DB_PASSWORD=<your-password>
DB_HOST=<database-host>
DB_PORT=5432
```

## 📝 Post-Deployment

1. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

2. **Create Admin User:**
   ```bash
   python manage.py createsuperuser
   ```

3. **Populate Sample Data:**
   ```bash
   python manage.py populate_data
   ```

4. **Test Your Site:**
   - Visit your deployed URL
   - Test restaurant listings
   - Test restaurant detail pages
   - Test admin panel

## 🐛 Troubleshooting

### Static Files Not Loading?
- Make sure `collectstatic` runs in build command
- Check `STATIC_ROOT` is set correctly
- Verify static files are being served

### Database Connection Errors?
- Double-check all database environment variables
- Verify database is running
- Check database credentials

### 500 Errors?
- Check application logs
- Verify `ALLOWED_HOSTS` includes your domain
- Make sure `DEBUG=False` in production
- Check for missing environment variables

### Can't Access Admin?
- Make sure you created superuser
- Check admin URL: `https://your-domain.com/admin/`

## 📚 Resources

- **Render Docs:** https://render.com/docs
- **Railway Docs:** https://docs.railway.app
- **Django Deployment:** https://docs.djangoproject.com/en/stable/howto/deployment/

---

**You're ready to deploy!** 🎉

Follow the steps above and your FoodieHub app will be live in minutes!

