
import os, json

CONFIG_FILE = ".gitamour.json"

DEFAULT = {
    "tone": "romantic",
    "identity": "solo"
}

def load():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE) as f:
            return json.load(f)
    return DEFAULT

def save(cfg):
    with open(CONFIG_FILE, "w") as f:
        json.dump(cfg, f, indent=2)
