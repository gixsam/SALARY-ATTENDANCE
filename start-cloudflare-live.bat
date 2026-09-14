@echo off
title Best Force Ltd - Cloudflare Live Tunnel Launcher
cd /d "%~dp0"

echo ===================================================================
echo   Best Force Ltd. - Salary Attendance & Payroll System
echo   Starting Localhost Web Server (127.0.0.1:8080)...
echo ===================================================================

start "PHP Server - Salary Attendance" /B php -S 127.0.0.1:8080

timeout /t 2 >nul

echo ===================================================================
echo   Starting Cloudflare Tunnel to expose localhost to the World...
echo ===================================================================

.\cloudflared.exe tunnel --url http://127.0.0.1:8080
pause
