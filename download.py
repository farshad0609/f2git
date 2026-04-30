import os
import requests

OUTPUT_DIR = "downloads"

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open("link.txt", "r") as f:
    links = [line.strip() for line in f if line.strip()]

for link in links:
    filename = link.split("/")[-1]
    path = os.path.join(OUTPUT_DIR, filename)

    print(f"Downloading {link} ...")
    r = requests.get(link, stream=True)
    r.raise_for_status()

    with open(path, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

print("Done.")
