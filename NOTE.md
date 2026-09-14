# 📋 BEST FORCE LTD. — SALARY ATTENDANCE & PAYROLL SYSTEM
## Master Project Note, Architecture & Changelog (`NOTE.md`)

> **Project Name:** Best Force Ltd. - Salary Attendance & Payroll System  
> **Company:** Best Force Ltd. (Best Outsourcing — Head Office)  
> **Local Project Root:** `D:\TECH\WEBSITE\SALARY ATTENDANCE\`  
> **Google Drive Workplace:** `G:\My Drive\ALL WEBSITE WORKPLACE\BEST FORCE LTD SALARY ATTENDENCE\`  
> **GitHub Repository:** [`https://github.com/gixsam/SALARY-ATTENDANCE`](https://github.com/gixsam/SALARY-ATTENDANCE)  
> **Technology Stack:** HTML5, Tailwind CSS, FontAwesome 6, xlsx-js-style, html2canvas, jsPDF, Vanilla JavaScript, PHP Built-in Server, Cloudflare Tunnel (`cloudflared`), Git & GitHub  
> **Live Local Server:** `http://127.0.0.1:8080`  
> **Live Cloudflare Tunnel:** `https://petroleum-echo-mirrors-rio.trycloudflare.com`  
> **Last Synchronized:** 2026-09-14 15:55 Local Time  

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

---

## 🏗️ 2. Architectural Blueprint & File Structure

```text
D:\TECH\WEBSITE\SALARY ATTENDANCE\
├── .gitignore                      <-- Excludes binaries (cloudflared.exe) and runtime logs
├── NOTE.md                         <-- Master project log & changelog (This file)
├── index.html                      <-- Complete Single-Page Application (Attendance Voucher, Payroll, Analytics, Modals)
├── logo.png                        <-- Official Best Force Ltd. company logo (cropped, clean transparent PNG)
├── logo-original.png               <-- Uncropped original uploaded logo asset
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
  - Built **Employee Master Database (25 Verified Staff)** pre-seeded with real Head Office staff records:
    - Jannatun Akter (18052), Sima Akter (18548), Md Atiqur Rahman (19058), Luchi Begum (1976), Md Arif Islam (17332), Bkash (15496), Md Firoz Ahmed (13770), Md Junayed Hossain (4646), Md Shumon Mia (18704), Md Takbir Hasan Rahat (17288), Md Shahidul Islam (10053), Md Abul Kalam (13111), Md Shahamim Sarker (15465), Ahad Mridah (4511), Md Sattar (5740), Md Ebad Ali (15166), Md Mamunur Rashid (6021), Afia Farjana Tandra (14248), Bedena Begum (18389), Md Shahariar Al Amin (9400), Md Jobaidul Islam Jahid (13697), ABM Rezaul Hadi (18355), Sk Tauhidul Islam Akash (14803), Md Khalilur Rahman (5900), Asma Neela (18293).
  - Integrated full **CRUD Operations** (Add, Edit, Single Delete, Multi-select Batch Delete, Factory Reset).
  - Built **Voucher Editing Modal** for financial adjustments (Basic Salary, Advance, Fine, Management Approval Note) and day-by-day manual punch entry (In/Out time, Approved Hours, Remarks).
  - Implemented **Export Engine**:
    - High-fidelity single and batch A4 PDF generation via `html2canvas` + `jsPDF`.
    - Formatted Excel workbooks (.xlsx) via `xlsx-js-style` with color styling.
  - Integrated **ZKTeco Biometric Importer** (Quick Paste modal + bulk textarea) and step-by-step hardware extraction instructions.

---

### [Update 002] — Cloudflare Live Tunnel & Localhost Daemon Integration
* **Date / Timestamp:** 2026-09-14 15:20 Local Time
* **Primary Files Created / Modified:** [`cloudflared.exe`](file:///d:/TECH/WEBSITE/SALARY%20ATTENDANCE/cloudflared.exe), [`cloudflared.log`](file:///d:/TECH/WEBSITE/SALARY%20ATTENDANCE/cloudflared.log), [`start-cloudflare-live.bat`](file:///d:/TECH/WEBSITE/SALARY%20ATTENDANCE/start-cloudflare-live.bat)
* **Summary of Changes:**
  - Integrated `cloudflared.exe` (v2026.3.0) into the project directory.
  - Started local background PHP web server on `127.0.0.1:8080`.
  - Initialized Cloudflare Quick Tunnel routing public internet traffic directly to `127.0.0.1:8080`.
  - Live Public URL established: `https://petroleum-echo-mirrors-rio.trycloudflare.com`.
  - Created `start-cloudflare-live.bat` enabling one-click startup of both local server and public Cloudflare tunnel.

---

### [Update 003] — Official Company Logo Integration & Optimization
* **Date / Timestamp:** 2026-09-14 15:38 Local Time
* **Primary Files Modified:** [`logo.png`](file:///d:/TECH/WEBSITE/SALARY%20ATTENDANCE/logo.png), [`logo-original.png`](file:///d:/TECH/WEBSITE/SALARY%20ATTENDANCE/logo-original.png), [`index.html`](file:///d:/TECH/WEBSITE/SALARY%20ATTENDANCE/index.html)
* **Summary of Changes:**
  - Received user's official Best Force Ltd company logo (`media_1789378650630.png`).
  - Cropped bottom AI generation watermark/smudge below wrist line (clean 938x888 resolution).
  - Replaced `logo.png` with the official logo with clean transparency.
  - Archived uncropped original as `logo-original.png`.
  - Added `<link rel="icon" type="image/png" href="logo.png">` in `index.html` `<head>` for browser tab branding.
  - Verified logo rendering in top navbar, A4 voucher header, and favicon over both `localhost:8080` and Cloudflare tunnel.

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
  - Initialized local Git repository, created `main` branch, linked `origin https://github.com/gixsam/SALARY-ATTENDANCE.git`.
  - Pushed initial release commit `386871c` containing complete source code, branding assets, and launchers.
  - Created `push-to-github.bat` for automatic staging, timestamped committing, pushing to GitHub, and copying `NOTE.md` to Google Drive.
  - Established permanent workflow: any future edits made by Antigravity AI will automatically be committed and pushed to GitHub.

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
| **GitHub Repository** | ✅ Connected & Pushed | `https://github.com/gixsam/SALARY-ATTENDANCE` | Main branch synced with commit `386871c` |
| **Local Web Server** | ✅ Active | `http://127.0.0.1:8080` | Running via PHP 8.3 CLI (Daemon Task 70) |
| **Cloudflare Tunnel** | ✅ Active | `https://petroleum-echo-mirrors-rio.trycloudflare.com` | Verified HTTP 200 via `cloudflared` (Daemon Task 78) |
| **Company Logo** | ✅ Active | `logo.png` | Official high-res logo with transparent background & favicon |
| **A4 Voucher Engine** | ✅ Verified | `index.html` (Tab 1) | Single/Batch A4 PDF & styled Excel workbooks |
| **Staff Database** | ✅ Verified | 25 Verified Records | LocalStorage (V5) cache with factory fallback |
| **Google Drive Sync** | ✅ Synchronized | `G:\My Drive\ALL WEBSITE WORKPLACE\BEST FORCE LTD SALARY ATTENDENCE\` | Mirror of `NOTE.md` synchronized |
