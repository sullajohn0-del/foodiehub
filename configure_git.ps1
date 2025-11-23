# Quick Git Configuration Script
# Run this to set up Git with your name and email

$env:Path += ";C:\Program Files\Git\bin"

Write-Host "`n=== Git Configuration ===" -ForegroundColor Cyan
Write-Host ""

Write-Host "Git needs to know who you are for commits." -ForegroundColor Yellow
Write-Host ""

$userName = Read-Host "Enter your name (e.g., John Doe)"
$userEmail = Read-Host "Enter your email (e.g., john@example.com)"

if ($userName -and $userEmail) {
    git config --global user.name $userName
    git config --global user.email $userEmail
    
    Write-Host ""
    Write-Host "✓ Git configured successfully!" -ForegroundColor Green
    Write-Host "  Name: $userName" -ForegroundColor White
    Write-Host "  Email: $userEmail" -ForegroundColor White
    Write-Host ""
    Write-Host "Now you can commit:" -ForegroundColor Yellow
    Write-Host "  git commit -m 'FoodieHub ready for deployment'" -ForegroundColor Cyan
    Write-Host ""
} else {
    Write-Host "Configuration cancelled." -ForegroundColor Yellow
}

