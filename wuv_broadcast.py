#!/usr/bin/env python3
"""
WUV Broadcaster
Spreads encouragement across repositories.
"""

import os
import random
import subprocess
from datetime import datetime

AFFIRMATIONS = [
    "Your commits matter.",
    "Someone will learn from this code.",
    "Progress beats perfection.",
    "Open source runs on kindness.",
    "Curiosity is seniority in training.",
]

def is_git_repo(path):
    return os.path.isdir(os.path.join(path, ".git"))

def spread_wuv(base_dir):
    for entry in os.listdir(base_dir):
        repo_path = os.path.join(base_dir, entry)

        if not is_git_repo(repo_path):
            continue

        msg = random.choice(AFFIRMATIONS)
        note_path = os.path.join(repo_path, "WUV_NOTE.txt")

        with open(note_path, "w") as f:
            f.write(f"WUV NOTE\n{msg}\nGenerated: {datetime.now()}\n")

        try:
            os.chdir(repo_path)
            subprocess.run(["git", "add", "WUV_NOTE.txt"], stdout=subprocess.DEVNULL)
        except Exception:
            pass

def main():
    base = os.getcwd()
    spread_wuv(base)

if __name__ == "__main__":
    main()
