import os
import requests
from urllib.parse import urlparse

OUTPUT_DIR = "downloads"

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open("link.txt", "r") as f:
    links = [line.strip() for line in f if line.strip()]

for i, link in enumerate(links):
    parsed = urlparse(link)
    filename = os.path.basename(parsed.path)

    if not filename:
        filename = f"file_{i}"

    path = os.path.join(OUTPUT_DIR, filename)

    print(f"Downloading {link} ...")

    r = requests.get(link, stream=True)
    r.raise_for_status()

    with open(path, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

print("Download complete.")
