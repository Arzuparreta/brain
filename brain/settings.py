import json
import os

from brain import config
from brain.paths import brain_root

settings = {k: getattr(config, k) for k in dir(config) if k.isupper()}

settings_path = brain_root() / "settings.json"
if settings_path.exists():
    with open(settings_path) as f:
        json_data = json.load(f)
        for k, v in json_data.items():
            if v not in ("", None):
                settings[k] = v

for k in settings:
    if k in os.environ:
        value = os.environ[k]
        if value.lower() in ("true", "false"):
            value = value.lower() == "true"
        settings[k] = value
