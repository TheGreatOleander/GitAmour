
import os, sys, subprocess
from datetime import datetime
from gitamour.messages import affirmation, poetic
from gitamour.streak import update
from gitamour.config import load
from gitamour.valentine import generate
from gitamour.animation import heart

def hook():
    git_dir = os.path.join(os.getcwd(), ".git")
    if not os.path.isdir(git_dir):
        print("Not in git repo.")
        return
    hook_path = os.path.join(git_dir, "hooks", "pre-commit")
    script = f'''#!/bin/sh
gitamour
'''
    with open(hook_path, "w") as f:
        f.write(script)
    os.chmod(hook_path, 0o755)
    print("Hook installed.")

def inject():
    cfg = load()
    msg = poetic(cfg["tone"])
    subprocess.run(["git", "commit", "-m", msg])

def message():
    cfg = load()
    print(poetic(cfg["tone"]))

def streak():
    s = update()
    print(f"Commit streak: {s} days.")

def valentine():
    print(generate())

def main():
    if len(sys.argv) == 1:
        heart()
        print(affirmation())
        return
    cmd = sys.argv[1]
    if cmd == "hook":
        hook()
    elif cmd == "inject":
        inject()
    elif cmd == "message":
        message()
    elif cmd == "streak":
        streak()
    elif cmd == "valentine":
        valentine()
    else:
        print(affirmation())
