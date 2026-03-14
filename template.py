import os
from pathlib import Path
import logging

# [TECH TERM: LOGGING] - This tracks exactly when folders are created.
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "universal_regression"

# [ARCHITECT LOGIC]: This list defines a ₹10,000 Cr project structure.
list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py", # The "Workers"
    f"src/{project_name}/utils/__init__.py",      # The "Tools"
    f"src/{project_name}/logging/__init__.py",   # The "logger"
    f"src/{project_name}/exception/__init__.py",  # The "Error handler"
    f"src/{project_name}/config/__init__.py",     # The "Control Room"
    f"src/{project_name}/pipeline/__init__.py",   # The "Orchestrator"
    f"src/{project_name}/entity/__init__.py",     # The "Data Rules"
    f"src/{project_name}/constants/__init__.py",  # The "Fixed Paths"
    "config/config.yaml", # Where you change data (House vs Gold)
    "params.yaml",        # Where you tune the Model Knobs
    "main.py",            # The Entry Point
    "requirements.txt",   # The Dependencies
    "setup.py",           # To install this project as a package
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")