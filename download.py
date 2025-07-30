from time import sleep
from pathlib import Path
import requests

with open(".cookie", "r") as f:
    session = f.read().strip()

for year in range(2015, 2025):
    for day in range(1, 26):
        if Path(f"{year}/{day:02d}/input.txt").is_file():
            continue
        print(f"Downloading input for {year} day {day:02d}...")
        cookies = {
            "session": session,
        }
        input = requests.get(
            f"https://adventofcode.com/{year}/day/{day}/input", cookies
        )

        folder = Path(f"{year}/{day:02d}")
        folder.mkdir(parents=True, exist_ok=True)
        with open(f"{folder}/input.txt", "w") as f:
            f.write(input.text.strip())
        sleep(5)
