import os
import json
import yaml
from src.universal_regression.logging import logger
from src.universal_regression.exception import CustomException
import sys
from pathlib import Path

# [CUSTOMIZE ZONE]: read_yaml
# WHY: This is the "Key" to your Control Room. It opens your .yaml files.
def read_yaml(path_to_yaml: Path):
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return content
    except Exception as e:
        # [SENIOR LOGIC]: We catch the error and pass it to our CustomException Doctor.
        raise CustomException(e, sys)

# [CUSTOMIZE ZONE]: create_directories
# WHY: This automatically creates the "artifacts" folders so you don't have to do it manually.
def create_directories(path_to_directories: list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

# [TECH TERM]: get_size
# WHY: This calculates the file size in KB so we can log it. 
# It helps us verify if the data download was actually successful.
def get_size(path: Path) -> str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


def save_json(path: Path, data: dict):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file saved at: {path}")