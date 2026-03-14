from pathlib import Path

# [NO-TOUCH ZONE]
# WHY: We define these as "Constants" (Capital letters) because they NEVER change.
# This makes it easy to find your config files from any part of the project.
CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")