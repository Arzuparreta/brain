import json
import os
import config

# Start with defaults from config.py
settings = {k: getattr(config, k) for k in dir(config) if k.isupper()}

# Load JSON overrides if file exists
if os.path.exists("settings.json"):
    with open("settings.json") as f:
        json_data = json.load(f)
        for k, v in json_data.items():
            # Only override if value is not empty / None
            if v not in ("", None):
                settings[k] = v

# Environment variable overrides (highest priority)
for k in settings:
    if k in os.environ:
        value = os.environ[k]
        if value.lower() in ("true", "false"):
            value = value.lower() == "true"
        settings[k] = value
