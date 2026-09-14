"""
Hostinger Direct FTP / FTPS Deployment Script for https://salary.best-travel.ltd
Usage:
    python deploy_to_hostinger_ftp.py --host <FTP_HOST> --user <FTP_USER> --password <FTP_PASS> [--target-dir <DIR>]
Or define environment variables / .ftp_config file:
    HOSTINGER_FTP_HOST=...
    HOSTINGER_FTP_USER=...
    HOSTINGER_FTP_PASS=...
"""

import os
import sys
import ftplib
import argparse

LOCAL_FILES = ["index.html", "logo.png", ".htaccess", "robots.txt"]

def upload_to_ftp(host, user, password, remote_dir="public_html", port=21, use_tls=True):
    print(f"[*] Connecting to {host}:{port}...")
    
    ftp = None
    if use_tls:
        try:
            ftp = ftplib.FTP_TLS()
            ftp.connect(host, port, timeout=30)
            ftp.login(user, password)
            ftp.prot_p()
            print("[+] Connected with FTPS (TLS).")
        except Exception as e:
            print(f"[-] FTPS failed ({e}), falling back to standard FTP...")
            ftp = ftplib.FTP()
            ftp.connect(host, port, timeout=30)
            ftp.login(user, password)
            print("[+] Connected with standard FTP.")
    else:
        ftp = ftplib.FTP()
        ftp.connect(host, port, timeout=30)
        ftp.login(user, password)

    # Change to target directory
    print(f"[*] Target directory: {remote_dir}")
    try:
        ftp.cwd(remote_dir)
    except Exception as e:
        print(f"[!] Could not change to {remote_dir}, listing current directory: {ftp.pwd()}")

    # Upload each file
    base_dir = os.path.dirname(os.path.abspath(__file__))
    for fname in LOCAL_FILES:
        fpath = os.path.join(base_dir, fname)
        if not os.path.exists(fpath):
            print(f"[-] Skipped missing file: {fname}")
            continue
        
        print(f"[*] Uploading {fname} ({os.path.getsize(fpath):,} bytes)...")
        with open(fpath, "rb") as fp:
            ftp.storbinary(f"STOR {fname}", fp)
        print(f"  [OK] Uploaded {fname}")

    ftp.quit()
    print("\n[SUCCESS] All files deployed to Hostinger!")
    print("Visit: https://salary.best-travel.ltd")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hostinger FTP Deployment")
    parser.add_argument("--host", default=os.getenv("HOSTINGER_FTP_HOST", "2.57.91.130"))
    parser.add_argument("--user", default=os.getenv("HOSTINGER_FTP_USER"))
    parser.add_argument("--password", default=os.getenv("HOSTINGER_FTP_PASS"))
    parser.add_argument("--target-dir", default=os.getenv("HOSTINGER_FTP_DIR", "public_html"))
    args = parser.parse_args()

    if not args.user or not args.password:
        print("Usage: python deploy_to_hostinger_ftp.py --host <FTP_HOST> --user <FTP_USER> --password <FTP_PASS> [--target-dir <DIR>]")
        print("\nOr configure HOSTINGER_FTP_USER and HOSTINGER_FTP_PASS environment variables.")
        sys.exit(1)

    upload_to_ftp(args.host, args.user, args.password, args.target_dir)
