@echo off
title Best Force Ltd - Salary Attendance & Payroll System
cd /d "%~dp0"
echo ==============================================================
echo   Best Force Ltd. - Salary Attendance & Payroll System
echo   Server running at http://localhost:8080
echo ==============================================================
start "" "http://localhost:8080"
php -S localhost:8080
pause
