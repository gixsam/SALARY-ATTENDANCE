import os
import zipfile
import shutil

source_dir = os.path.dirname(os.path.abspath(__file__))
output_zip = os.path.join(source_dir, "salary_best_travel_ltd_upload.zip")
gdrive_dir = r"G:\My Drive\ALL WEBSITE WORKPLACE\BEST FORCE LTD SALARY ATTENDENCE"

# Production files to include in Hostinger File Manager upload
files_to_pack = [
    "index.html",
    "logo.png",
    ".htaccess",
    "robots.txt"
]

temp_zip = output_zip + ".tmp"
if os.path.exists(temp_zip):
    os.remove(temp_zip)

with zipfile.ZipFile(temp_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
    for fname in files_to_pack:
        fpath = os.path.join(source_dir, fname)
        if os.path.exists(fpath):
            zipf.write(fpath, fname)
            print(f"  + Added: {fname} ({os.path.getsize(fpath):,} bytes)")
        else:
            print(f"  ! Warning: {fname} not found!")

if os.path.exists(output_zip):
    os.remove(output_zip)
os.rename(temp_zip, output_zip)

print(f"\n[SUCCESS] Hostinger Production ZIP created:")
print(f"  Location: {output_zip} ({os.path.getsize(output_zip):,} bytes)")

# Mirror to Google Drive Workplace if directory exists
if os.path.exists(gdrive_dir):
    gdrive_zip = os.path.join(gdrive_dir, "salary_best_travel_ltd_upload.zip")
    shutil.copy2(output_zip, gdrive_zip)
    print(f"  Google Drive Mirror: {gdrive_zip}")
