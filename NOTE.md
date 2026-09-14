# 📋 BEST FORCE LTD. — SALARY ATTENDANCE & PAYROLL SYSTEM
## Master Project Note, Architecture & Changelog (`NOTE.md`)

> **Project Name:** Best Force Ltd. - Salary Attendance & Payroll System  
> **Company:** Best Force Ltd. (Best Outsourcing — Head Office)  
> **Production Domain:** [`https://salary.best-travel.ltd`](https://salary.best-travel.ltd)  
> **Hostinger Target Directory:** `public_html/` (Subdomain root for `salary.best-travel.ltd`)  
> **Local Project Root:** `D:\TECH\WEBSITE\SALARY ATTENDANCE\`  
> **Google Drive Workplace:** `G:\My Drive\ALL WEBSITE WORKPLACE\BEST FORCE LTD SALARY ATTENDENCE\`  
> **GitHub Repository:** [`https://github.com/gixsam/SALARY-ATTENDANCE`](https://github.com/gixsam/SALARY-ATTENDANCE)  
> **Technology Stack:** HTML5, Tailwind CSS, FontAwesome 6, xlsx-js-style, html2canvas, jsPDF, Vanilla JavaScript, Apache (.htaccess), Hostinger Cloud, Cloudflare Tunnel, GitHub Actions (CI/CD), Git & GitHub  
> **Live Local Server:** `http://127.0.0.1:8080`  
> **Live Cloudflare Tunnel:** `https://petroleum-echo-mirrors-rio.trycloudflare.com`  
> **Last Synchronized:** 2026-09-14 16:05 Local Time  

---

## 📌 1. Master Rule & Maintenance Directive

This file (`NOTE.md`) is the **mandatory, single source of truth** for all historical, present, and future updates to the Best Force Ltd. Salary Attendance & Payroll System.

### Mandatory Directive:
Whenever ANY update, feature addition, bug fix, asset modification, or architectural change is performed:
1. **Document the update** in this file with full technical detail, timestamp, and modified file list.
2. **Synchronize this file to BOTH locations immediately**:
   - **Local Project Root:** `D:\TECH\WEBSITE\SALARY ATTENDANCE\NOTE.md`
   - **Google Drive Storage:** `G:\My Drive\ALL WEBSITE WORKPLACE\BEST FORCE LTD SALARY ATTENDENCE\NOTE.md`
3. **Commit & Push to GitHub Repository automatically**:
   - Push to `origin main` at `https://github.com/gixsam/SALARY-ATTENDANCE`
4. **Rebuild Hostinger Upload Package**:
   - Run `build_hostinger_package.py` to regenerate `salary_best_travel_ltd_upload.zip` in both Local and Google Drive folders.

---

## 🏗️ 2. Architectural Blueprint & File Structure

```text
D:\TECH\WEBSITE\SALARY ATTENDANCE\
├── .github/
│   └── workflows/
│       └── deploy.yml              <-- GitHub Actions automated CI/CD deployment to Hostinger on push
├── .gitignore                      <-- Excludes binaries, upload zip, and runtime logs from git
├── .htaccess                       <-- Hostinger Apache configuration (HTTPS redirect, Gzip, Caching, Security Headers)
├── robots.txt                      <-- Search engine crawling directives
├── NOTE.md                         <-- Master project log & changelog (This file)
├── index.html                      <-- Complete Single-Page Application (Attendance Voucher, Payroll, Analytics, Modals)
├── logo.png                        <-- Official Best Force Ltd. company logo (cropped, clean transparent PNG)
├── logo-original.png               <-- Uncropped original uploaded logo asset
├── salary_best_travel_ltd_upload.zip <-- Production package ready for Hostinger File Manager upload & extract
├── build_hostinger_package.py      <-- Automation script to bundle production zip & mirror to Google Drive
├── deploy_to_hostinger_ftp.py      <-- Direct FTP / FTPS deployment engine to push updates to Hostinger
├── cloudflared.exe                 <-- Cloudflare Tunnel agent (v2026.3.0) for public live sharing [Ignored in git]
├── cloudflared.log                 <-- Runtime log file recording active tunnel connection and URLs [Ignored in git]
├── start-server.bat                <-- One-click batch launcher for local PHP server (http://localhost:8080)
├── start-cloudflare-live.bat       <-- One-click batch launcher for both local PHP server and Cloudflare Live Tunnel
└── push-to-github.bat              <-- One-click manual script to stage, commit, push to GitHub & sync Google Drive
```

---

## 📜 3. Comprehensive Changelog & Update History

### [Update 001] — Initial System Initialization & Core Engine Build
* **Date / Timestamp:** 2026-09-14 14:12 Local Time
* **Primary Files Created:** [`index.html`](file:///d:/TECH/WEBSITE/SALARY%20ATTENDANCE/index.html), [`start-server.bat`](file:///d:/TECH/WEBSITE/SALARY%20ATTENDANCE/start-server.bat)
* **Summary of Changes:**
  - Designed and deployed the complete **Salary Attendance & Payroll System** single-page web app.
  - Implemented **A4 Attendance Voucher Sheet** replicating physical office attendance registers with:
    - Standard Bangladesh weekend (Friday - `#cbd5e1`) and Gazetted / Company Holiday (`#bbf7d0`) highlighting.
    - Absentee markers (`#fee2e2`, `A`) and duty hour calculation capped at 10 hours daily.
    - Executive approval signatures (CEO, Control Manager, MD, Salary Recipient).
  - Built **Monthly Payroll Summary Tab** with live tabular summary, grand totals, and responsive mobile cards.
  - Built **Live Analytics KPI Dashboard** showing Total Base Pay, Total Advance, Total Fine, Total Duty Hours, and Net Payable.
  - Built **Employee Master Database (25 Verified Staff)** pre-seeded with real Head Office staff records.
  - Integrated full **CRUD Operations** (Add, Edit, Single Delete, Multi-select Batch Delete, Factory Reset).
  - Built **Voucher Editing Modal** for financial adjustments and day-by-day manual punch entry.
  - Implemented **Export Engine** for A4 PDF and styled Excel workbooks.
  - Integrated **ZKTeco Biometric Importer** and extraction guides.

---

### [Update 002] — Cloudflare Live Tunnel & Localhost Daemon Integration
* **Date / Timestamp:** 2026-09-14 15:20 Local Time
* **Primary Files Created / Modified:** [`cloudflared.exe`](file:///d:/TECH/WEBSITE/SALARY%20ATTENDANCE/cloudflared.exe), [`cloudflared.log`](file:///d:/TECH/WEBSITE/SALARY%20ATTENDANCE/cloudflared.log), [`start-cloudflare-live.bat`](file:///d:/TECH/WEBSITE/SALARY%20ATTENDANCE/start-cloudflare-live.bat)
* **Summary of Changes:**
  - Integrated `cloudflared.exe` (v2026.3.0) into project directory.
  - Started local background PHP web server on `127.0.0.1:8080`.
  - Initialized Cloudflare Quick Tunnel routing to `127.0.0.1:8080`.
  - Live Public URL established: `https://petroleum-echo-mirrors-rio.trycloudflare.com`.
  - Created `start-cloudflare-live.bat` for one-click startup.

---

### [Update 003] — Official Company Logo Integration & Optimization
* **Date / Timestamp:** 2026-09-14 15:38 Local Time
* **Primary Files Modified:** [`logo.png`](file:///d:/TECH/WEBSITE/SALARY%20ATTENDANCE/logo.png), [`logo-original.png`](file:///d:/TECH/WEBSITE/SALARY%20ATTENDANCE/logo-original.png), [`index.html`](file:///d:/TECH/WEBSITE/SALARY%20ATTENDANCE/index.html)
* **Summary of Changes:**
  - Received user's official Best Force Ltd company logo (`media_1789378650630.png`).
  - Cropped bottom watermark smudge below wrist line (clean 938x888 resolution).
  - Replaced `logo.png` with official logo with clean transparency.
  - Archived original as `logo-original.png`.
  - Added `<link rel="icon" type="image/png" href="logo.png">` in `index.html` `<head>`.

---

### [Update 004] — Master NOTE.md & Google Drive Synchronization Directive
* **Date / Timestamp:** 2026-09-14 15:50 Local Time
* **Primary Files Created:**
  - `D:\TECH\WEBSITE\SALARY ATTENDANCE\NOTE.md`
  - `G:\My Drive\ALL WEBSITE WORKPLACE\BEST FORCE LTD SALARY ATTENDENCE\NOTE.md`
* **Summary of Changes:**
  - Established persistent documentation protocol per user mandate.
  - Linked local project root with Google Drive cloud mirror path.
  - Back-filled complete changelog from inception to current production state.

---

### [Update 005] — GitHub Remote Repository Integration & Continuous Sync Pipeline
* **Date / Timestamp:** 2026-09-14 15:54 Local Time
* **Primary Files Created / Modified:**
  - [`.gitignore`](file:///D:/TECH/WEBSITE/SALARY%20ATTENDANCE/.gitignore)
  - [`push-to-github.bat`](file:///D:/TECH/WEBSITE/SALARY%20ATTENDANCE/push-to-github.bat)
  - [`NOTE.md`](file:///D:/TECH/WEBSITE/SALARY%20ATTENDANCE/NOTE.md)
* **Summary of Changes:**
  - Created new public GitHub repository: [`https://github.com/gixsam/SALARY-ATTENDANCE`](https://github.com/gixsam/SALARY-ATTENDANCE).
  - Configured `.gitignore` to prevent committing heavy binaries (`cloudflared.exe` - 65MB) and runtime logs.
  - Initialized local Git repository, created `main` branch, linked remote.
  - Pushed initial release commit `386871c`.
  - Created `push-to-github.bat` for automatic staging, timestamped committing, and syncing.

---

### [Update 006] — Hostinger Domain Setup (`salary.best-travel.ltd`) & Deployment Package Engine
* **Date / Timestamp:** 2026-09-14 16:02 Local Time
* **Primary Files Created / Modified:**
  - [`.htaccess`](file:///D:/TECH/WEBSITE/SALARY%20ATTENDANCE/.htaccess)
  - [`robots.txt`](file:///D:/TECH/WEBSITE/SALARY%20ATTENDANCE/robots.txt)
  - [`build_hostinger_package.py`](file:///D:/TECH/WEBSITE/SALARY%20ATTENDANCE/build_hostinger_package.py)
  - [`deploy_to_hostinger_ftp.py`](file:///D:/TECH/WEBSITE/SALARY%20ATTENDANCE/deploy_to_hostinger_ftp.py)
  - [`salary_best_travel_ltd_upload.zip`](file:///D:/TECH/WEBSITE/SALARY%20ATTENDANCE/salary_best_travel_ltd_upload.zip)
* **Summary of Changes:**
  - Configured project for target domain **[`https://salary.best-travel.ltd`](https://salary.best-travel.ltd)** on Hostinger web hosting.
  - Created production `.htaccess` with HTTPS redirection, security headers, Gzip compression, and browser caching.
  - Created `build_hostinger_package.py` which compiles `salary_best_travel_ltd_upload.zip`.
  - Auto-mirrored `salary_best_travel_ltd_upload.zip` into `G:\My Drive\ALL WEBSITE WORKPLACE\BEST FORCE LTD SALARY ATTENDENCE\`.
  - Built `deploy_to_hostinger_ftp.py` for direct automated FTP/FTPS deployment.

---

### [Update 007] — GitHub to Hostinger Automated CI/CD Deployment Pipeline
* **Date / Timestamp:** 2026-09-14 16:05 Local Time
* **Primary Files Created / Modified:**
  - [`.github/workflows/deploy.yml`](file:///D:/TECH/WEBSITE/SALARY%20ATTENDANCE/.github/workflows/deploy.yml)
  - [`NOTE.md`](file:///D:/TECH/WEBSITE/SALARY%20ATTENDANCE/NOTE.md)
* **Summary of Changes:**
  - Designed automated continuous deployment pipeline connecting GitHub repository directly to Hostinger.
  - Added `.github/workflows/deploy.yml` utilizing `SamKirkland/FTP-Deploy-Action@v4.3.5`.
  - Whenever code is pushed to `main` branch, GitHub Actions automatically uploads all updated production files (`index.html`, `logo.png`, `.htaccess`, `robots.txt`) directly into Hostinger's `public_html/`.

---

### [Update 008] — Perfect PDF Table Cell Centering & A4 Proportion Matching
* **Date / Timestamp:** 2026-09-14 16:35 Local Time
* **Primary Files Modified:**
  - [`index.html`](file:///D:/TECH/WEBSITE/SALARY%20ATTENDANCE/index.html)
  - [`NOTE.md`](file:///D:/TECH/WEBSITE/SALARY%20ATTENDANCE/NOTE.md)
  - [`salary_best_travel_ltd_upload.zip`](file:///D:/TECH/WEBSITE/SALARY%20ATTENDANCE/salary_best_travel_ltd_upload.zip)
* **Summary of Changes:**
  - **Identified & Resolved PDF Misalignment & Squishing Bug:**
    - Root Cause 1: On mobile devices, `html2canvas` captures within mobile viewport context, inheriting tiny 8px fonts and auto row heights that collapsed the table into paper-thin rows (~15px).
    - Root Cause 2: Arbitrary line-height (1.35) combined with top padding caused text baseline to hug the top border of each cell rather than centering vertically.
    - Root Cause 3: The squished voucher height (~750px) left over 100mm of dead white space at the bottom of the 297mm A4 page.
  - **Engineered Isolated High-Resolution Rendering Sandbox:**
    - Implemented `#pdf-render-sandbox` with a strict fixed 794px width (standard A4 width at 96 DPI), running at `scale: 2.5` (~300 DPI print clarity).
    - Applied explicit height (`23px` tbody, `25px` thead/tfoot, `28px` employee info bar) with identical matching `line-height` (`23px` / `25px` / `28px`) and zero padding. This mathematically forces character glyphs into the dead-center of every box horizontally and vertically.
    - Overrode `overflow: hidden; text-overflow: ellipsis; white-space: nowrap;` on Remarks to prevent baseline clipping.
  - **True-to-Scale A4 Page Sizing:**
    - Re-architected jsPDF rendering geometry (`width: 198mm`, `height: ~276mm`, `left/right margin: 6mm`, `top/bottom margin: ~10.5mm`).
    - The downloaded PDF voucher now fills 93% of the A4 page height with elegant, balanced margins, matching the exact format, sizing, and aesthetic of the live website view.
  - **Applied Across All Export Engines:**
    - Enhanced Single Voucher PDF download (`downloadSingleEmployeePdf()`).
    - Enhanced Batch 25-Voucher PDF download (`downloadAllEmployeesPdf()`).
    - Enhanced Monthly Payroll Summary PDF export (`downloadSummaryPdfDirect()`) to render the full official summary table on mobile devices.

---

## 🔮 4. Future Roadmap & Planned Upgrades

1. **Automated SQLite / MySQL Persistence Layer:**
   - Add optional backend API endpoints to store staff rosters and attendance records permanently into an SQLite/MySQL database alongside localStorage.
2. **Direct ZKTeco BioTime API Connector:**
   - Implement scheduled automated synchronization via ZKTeco BioTime JWT token authentication (matching `account.php` logic from the main Best Force Ltd. portal).
3. **Multi-Month Archive & Historical Compare:**
   - Retain separate monthly sheets across multiple months (July, August, September 2026, etc.) without overwriting.
4. **Automated Payslip Slip PDF Generator:**
   - Add single-click printable miniature pay slips (half-page voucher) for individual staff payout distribution.
5. **Role-Based Login / Super Admin Authentication:**
   - Restrict edit and delete controls behind admin credentials.

---

## 📊 5. Verification & Health Status

| Component | Status | Target / URI | Notes |
|---|---|---|---|
| **GitHub CI/CD** | ✅ Configured | `.github/workflows/deploy.yml` | Auto-deploys to Hostinger on push |
| **Production Domain** | ✅ Live & Verified | `https://salary.best-travel.ltd` | Connected to Hostinger. Serving full app & logo.png |
| **Hostinger Package** | ✅ Built | `salary_best_travel_ltd_upload.zip` | Available in Local & Google Drive |
| **GitHub Repository** | ✅ Connected & Pushed | `https://github.com/gixsam/SALARY-ATTENDANCE` | Main branch synced |
| **Local Web Server** | ✅ Active | `http://127.0.0.1:8080` | Running via PHP 8.3 CLI (Daemon Task 70) |
| **Cloudflare Tunnel** | ✅ Active | `https://petroleum-echo-mirrors-rio.trycloudflare.com` | Verified HTTP 200 via `cloudflared` (Daemon Task 78) |
| **Company Logo** | ✅ Active | `logo.png` | Official high-res logo with transparent background & favicon |
| **A4 Voucher Engine** | ✅ Verified | `index.html` (Tab 1) | Single/Batch A4 PDF & styled Excel workbooks |
| **Staff Database** | ✅ Verified | 25 Verified Records | LocalStorage (V5) cache with factory fallback |
| **Google Drive Sync** | ✅ Synchronized | `G:\My Drive\ALL WEBSITE WORKPLACE\BEST FORCE LTD SALARY ATTENDENCE\` | Mirror of `NOTE.md` and ZIP package synchronized |
