@echo off
title Push to GitHub & Sync Google Drive - Best Force Ltd
cd /d "%~dp0"

echo ===================================================================
echo   Best Force Ltd. - Salary Attendance System
echo   Step 1: Syncing NOTE.md to Google Drive Workplace...
echo ===================================================================

copy /Y "NOTE.md" "G:\My Drive\ALL WEBSITE WORKPLACE\BEST FORCE LTD SALARY ATTENDENCE\NOTE.md" >nul
if %ERRORLEVEL% EQU 0 (
    echo   [OK] NOTE.md successfully synced to Google Drive.
) else (
    echo   [WARNING] Could not sync to Google Drive. Ensure G: drive is mounted.
)

echo ===================================================================
echo   Step 2: Staging, Committing and Pushing to GitHub...
echo ===================================================================

git add .
git commit -m "Update: %date% %time%"
git push origin main

echo ===================================================================
echo   Push & Sync complete!
echo   Repository: https://github.com/gixsam/SALARY-ATTENDANCE
echo ===================================================================
timeout /t 3 >nul
