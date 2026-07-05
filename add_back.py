import re, os

files_and_targets = {
    "legal.html": "index.html",
    "wallpapers.html": "index.html",
    "jailbreaks.html": "index.html",
    "repos.html": "index.html",
    "certificates.html": "index.html",
    "survey.html": "index.html",
    "websites.html": "index.html",
    "ipa/index.html": "../index.html",
    "wallpapers/aapl_os_wallpapers/index.html": "../../wallpapers.html",
    "wallpapers/aapl_device_wallpapers/index.html": "../../wallpapers.html",
    "wallpapers/appl_50th_anniversary/index.html": "../../wallpapers.html",
    "wallpapers/aapl_park/index.html": "../../wallpapers.html",
}

for path, target in files_and_targets.items():
    if not os.path.exists(path):
        print("SKIPPING")
        continue

    with open(path, "r", encoding="utf-8") as file:
        content = file.read()

    if 'class="back-button"' in content:
        print("Already exists, SKIPPING!")
        continue
    
    back_link = f'    <a class="back-button" href="{target}">&larr; Back</a>\n'

    new_content, n = re.subn(r'(<body[^>]*>\n)', r'\1' + back_link, content, count=1)
    if n == 0:
        print("No Body Tag found.")
        continue

    with open(path, "w", encoding="utf-8") as file_new:
        file_new.write(new_content)
    print(f"Updated {path} with backlink to {target}")
