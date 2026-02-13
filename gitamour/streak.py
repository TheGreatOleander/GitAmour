
import os
from datetime import datetime

FILE = ".gitamour_streak"

def update():
    today = datetime.now().date()
    if not os.path.exists(FILE):
        with open(FILE, "w") as f:
            f.write(str(today) + "\n1")
        return 1

    with open(FILE) as f:
        last, count = f.read().splitlines()
    last = datetime.fromisoformat(last).date()
    count = int(count)

    if today > last:
        count += 1

    with open(FILE, "w") as f:
        f.write(str(today) + f"\n{count}")

    return count
