# 🚀 Start Deployment - Step by Step

## Step 1: Initialize Git Repository (If Not Done)

```powershell
cd C:\Users\sulla\OneDrive\Desktop\shop\myproject

# Check if git is initialized
git status

# If not initialized, run:
git init
git add .
git commit -m "FoodieHub - Initial commit ready for deployment"
```

## Step 2: Create GitHub Repository

1. Go to https://github.com and sign in
2. Click the **+** icon → **New repository**
3. Repository name: `foodiehub` (or any name you prefer)
4. Description: "Filipino Food Delivery App - FoodieHub"
5. Choose **Public** or **Private**
6. **DO NOT** initialize with README, .gitignore, or license
7. Click **Create repository**

## Step 3: Push to GitHub

After creating the repository, GitHub will show you commands. Use these:

```powershell
cd C:\Users\sulla\OneDrive\Desktop\shop\myproject

# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/foodiehub.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

## Step 4: Deploy to Render

### 4.1 Create Render Account
1. Go to https://render.com
2. Click **Get Started for Free**
3. Sign up with your GitHub account (recommended)

### 4.2 Create PostgreSQL Database
1. In Render dashboard, click **New +** → **PostgreSQL**
2. Settings:
   - **Name:** `foodiehub-db`
   - **Database:** `foodiehub` (or leave default)
   - **User:** (auto-generated)
   - **Region:** Choose closest to you
   - **Plan:** Free
3. Click **Create Database**
4. **IMPORTANT:** Copy these values (you'll need them):
   - Internal Database URL (looks like: `postgresql://user:password@host:port/dbname`)
   - Or copy individual values:
     - Database Name
     - User
     - Password
     - Host
     - Port (usually 5432)

### 4.3 Create Web Service
1. Click **New +** → **Web Service**
2. Connect your GitHub account (if not already)
3. Select your `foodiehub` repository
4. Configure:
   - **Name:** `foodiehub`
   - **Region:** Same as database
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

### 4.4 Set Environment Variables
Click on **Environment** tab and add these:

```
DEBUG=False
SECRET_KEY=sppvp^%=oz46#j^)mf4tg7ocs0tpay$setn%^#*ch3*%nntav@
ALLOWED_HOSTS=your-app-name.onrender.com
```

**Database Variables** (from your PostgreSQL database):
```
DB_NAME=<from-render-database>
DB_USER=<from-render-database>
DB_PASSWORD=<from-render-database>
DB_HOST=<from-render-database>
DB_PORT=5432
```

**Note:** Replace `your-app-name.onrender.com` with your actual Render app URL (you'll see it after creation).

### 4.5 Deploy!
1. Click **Create Web Service**
2. Wait 5-10 minutes for deployment
3. Your app will be live at: `https://your-app-name.onrender.com`

## Step 5: Run Migrations & Setup

After deployment completes:

1. Go to your Web Service in Render dashboard
2. Click on **Shell** tab (or **Logs** to see deployment status)
3. In the Shell, run:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py populate_data
```

Follow prompts to create admin user.

## Step 6: Test Your Deployed App

1. Visit your app URL: `https://your-app-name.onrender.com`
2. Test:
   - Home page with restaurants
   - Restaurant detail pages
   - Menu items
   - Admin panel: `https://your-app-name.onrender.com/admin/`

## 🎉 You're Live!

Your FoodieHub app is now deployed and accessible worldwide!

## 📝 Quick Reference

### Your App URLs:
- **Home:** `https://your-app-name.onrender.com`
- **Admin:** `https://your-app-name.onrender.com/admin/`

### To Update Your App:
```powershell
# Make changes locally
git add .
git commit -m "Your update message"
git push origin main

# Render will automatically redeploy!
```

### To View Logs:
- Go to Render dashboard → Your Web Service → **Logs** tab

### To Run Commands:
- Go to Render dashboard → Your Web Service → **Shell** tab

## 🆘 Need Help?

- **Render Docs:** https://render.com/docs
- **Render Support:** Check their help center
- **Django Docs:** https://docs.djangoproject.com/

---

**Ready? Start with Step 1 above!** 🚀

