# ✅ FoodieHub Deployment - Simple Checklist

## 📋 Step-by-Step Checklist

### Phase 1: Install Git ⏱️ 5 minutes
- [ ] **Download Git**
  - ✅ Git download page opened in your browser
  - [ ] Click "Download for Windows"
  - [ ] Save the installer file

- [ ] **Install Git**
  - [ ] Run the installer
  - [ ] Click "Next" through all steps (use defaults)
  - [ ] **Important:** When asked about PATH, choose:
    - ✅ "Git from the command line and also from 3rd-party software"
  - [ ] Complete installation
  - [ ] **Restart PowerShell** (close and reopen)

- [ ] **Verify Installation**
  ```powershell
  git --version
  ```
  Should show: `git version 2.x.x`

---

### Phase 2: Setup Git Repository ⏱️ 5 minutes
- [ ] **Run Setup Helper**
  ```powershell
  cd C:\Users\sulla\OneDrive\Desktop\shop\myproject
  .\setup_git.ps1
  ```

- [ ] **Initialize Repository** (if not done by script)
  ```powershell
  git init
  git add .
  git commit -m "FoodieHub ready for deployment"
  ```

---

### Phase 3: Create GitHub Repository ⏱️ 3 minutes
- [ ] **Go to GitHub**
  - [ ] Visit: https://github.com
  - [ ] Sign in or create account

- [ ] **Create New Repository**
  - [ ] Click "+" → "New repository"
  - [ ] Name: `foodiehub`
  - [ ] Description: "Filipino Food Delivery App"
  - [ ] Choose Public or Private
  - [ ] **DO NOT** check "Initialize with README"
  - [ ] Click "Create repository"

---

### Phase 4: Push to GitHub ⏱️ 2 minutes
- [ ] **Connect to GitHub**
  ```powershell
  git remote add origin https://github.com/YOUR_USERNAME/foodiehub.git
  git branch -M main
  git push -u origin main
  ```
  (Replace YOUR_USERNAME with your GitHub username)

---

### Phase 5: Deploy to Render ⏱️ 10 minutes
- [ ] **Create Render Account**
  - [ ] Go to: https://render.com
  - [ ] Sign up (use GitHub account - easier!)

- [ ] **Create PostgreSQL Database**
  - [ ] Click "New +" → "PostgreSQL"
  - [ ] Name: `foodiehub-db`
  - [ ] Plan: Free
  - [ ] Click "Create Database"
  - [ ] **COPY these values** (you'll need them):
    - Database Name
    - User
    - Password
    - Host
    - Port (usually 5432)

- [ ] **Create Web Service**
  - [ ] Click "New +" → "Web Service"
  - [ ] Connect GitHub account
  - [ ] Select "foodiehub" repository
  - [ ] Configure:
    - Name: `foodiehub`
    - Build Command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
    - Start Command: `gunicorn myproject.wsgi:application`
    - Plan: Free

- [ ] **Set Environment Variables**
  Go to "Environment" tab and add:
  ```
  DEBUG=False
  SECRET_KEY=sppvp^%=oz46#j^)mf4tg7ocs0tpay$setn%^#*ch3*%nntav@
  ALLOWED_HOSTS=your-app-name.onrender.com
  DB_NAME=<paste-from-render>
  DB_USER=<paste-from-render>
  DB_PASSWORD=<paste-from-render>
  DB_HOST=<paste-from-render>
  DB_PORT=5432
  ```

- [ ] **Deploy**
  - [ ] Click "Create Web Service"
  - [ ] Wait 5-10 minutes for deployment
  - [ ] Watch the logs for progress

---

### Phase 6: Setup Database ⏱️ 3 minutes
- [ ] **Run Migrations**
  - [ ] Go to your Web Service in Render
  - [ ] Click "Shell" tab
  - [ ] Run:
    ```bash
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py populate_data
    ```
  - [ ] Follow prompts to create admin user

---

### Phase 7: Test Your App ⏱️ 2 minutes
- [ ] **Visit Your App**
  - [ ] Go to: `https://your-app-name.onrender.com`
  - [ ] Test home page
  - [ ] Test restaurant pages
  - [ ] Test admin: `https://your-app-name.onrender.com/admin/`

---

## 🎉 Success!

If all steps are checked, your FoodieHub app is live!

## 📝 Notes

- **Secret Key:** Save this somewhere safe: `sppvp^%=oz46#j^)mf4tg7ocs0tpay$setn%^#*ch3*%nntav@`
- **Total Time:** ~30 minutes
- **Need Help?** Check DEPLOYMENT_QUICK_START.txt or START_DEPLOYMENT.md

---

**Current Status:** ✅ Git download page opened - Start with Phase 1!

