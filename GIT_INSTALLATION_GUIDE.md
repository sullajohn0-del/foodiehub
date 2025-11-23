# 📥 Git Installation Guide - Step by Step

## 🎯 What You Need to Do

The Git download page should be open in your browser. Follow these exact steps:

## Step 1: Download Git

1. **On the Git download page:**
   - Look for the big "Download for Windows" button
   - Click it
   - The file will start downloading (usually `Git-2.x.x-64-bit.exe`)

2. **Wait for download to complete**
   - Check your Downloads folder
   - File size: ~50-60 MB

## Step 2: Run the Installer

1. **Find the downloaded file:**
   - Usually in: `C:\Users\sulla\Downloads\`
   - File name: `Git-2.x.x-64-bit.exe`

2. **Double-click the file** to run the installer

3. **If Windows asks for permission:**
   - Click "Yes" or "Run"

## Step 3: Installation Wizard

### Screen 1: License Information
- Click **"Next"**

### Screen 2: Select Destination Location
- Use default location
- Click **"Next"**

### Screen 3: Select Components ⚠️ IMPORTANT
- Keep all defaults checked
- Click **"Next"**

### Screen 4: Select Start Menu Folder
- Use default
- Click **"Next"**

### Screen 5: Choosing the default editor
- Default is fine (usually "Use Visual Studio Code" or "Nano")
- Click **"Next"**

### Screen 6: Adjusting your PATH environment ⚠️ CRITICAL
**THIS IS THE MOST IMPORTANT STEP!**

Choose:
- ✅ **"Git from the command line and also from 3rd-party software"**

**DO NOT choose:**
- ❌ "Use Git from Git Bash only"
- ❌ "Use Git and optional Unix tools from the Command Prompt"

Click **"Next"**

### Screen 7: Choosing HTTPS transport backend
- Use default (OpenSSL)
- Click **"Next"**

### Screen 8: Configuring the line ending conversions
- Use default ("Checkout Windows-style, commit Unix-style line endings")
- Click **"Next"**

### Screen 9: Configuring the terminal emulator
- Use default ("Use Windows' default console window")
- Click **"Next"**

### Screen 10: Configuring extra options
- Use defaults
- Click **"Next"**

### Screen 11: Configuring experimental options
- Leave unchecked (or use defaults)
- Click **"Install"**

## Step 4: Installation Progress

- Wait for installation to complete (1-2 minutes)
- You'll see a progress bar
- When done, click **"Finish"**

## Step 5: Verify Installation

1. **Close PowerShell completely** (if it's open)

2. **Open a NEW PowerShell window**

3. **Navigate to your project:**
   ```powershell
   cd C:\Users\sulla\OneDrive\Desktop\shop\myproject
   ```

4. **Check if Git works:**
   ```powershell
   git --version
   ```

   **Expected output:**
   ```
   git version 2.43.0 (or similar)
   ```

5. **If you see a version number:**
   - ✅ Git is installed correctly!
   - Run: `.\check_git.ps1` to verify
   - Then run: `.\setup_git.ps1` to continue

## ❌ Troubleshooting

### "git is not recognized"
- **Solution:** Restart PowerShell (close and reopen)
- If still not working, restart your computer
- Make sure you chose "Git from the command line" during installation

### Installation fails
- Make sure you have admin rights
- Try running installer as Administrator
- Check if antivirus is blocking it

### Can't find the download
- Check your Downloads folder
- Or download again from: https://git-scm.com/download/win

## ✅ After Installation

Once Git is installed and verified:

1. Run: `.\check_git.ps1`
2. Run: `.\setup_git.ps1`
3. Follow: `DEPLOYMENT_CHECKLIST_SIMPLE.md`

---

**Need help?** If you get stuck at any step, let me know which screen you're on!

