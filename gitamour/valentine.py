
import os, subprocess
from datetime import datetime

def generate():
    try:
        commits = subprocess.check_output(["git", "rev-list", "--count", "HEAD"]).decode().strip()
    except:
        commits = "many"

    content = f"""# VALENTINE

This repository has {commits} commits of devotion.

Built with persistence.
Refined with care.
Committed with heart.

Generated on {datetime.now()}.
"""

    with open("VALENTINE.md", "w") as f:
        f.write(content)

    return "VALENTINE.md created."
