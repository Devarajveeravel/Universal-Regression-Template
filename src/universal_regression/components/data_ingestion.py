import os
import urllib.request as request
import zipfile
import ssl # Keep this import
from src.universal_regression.logging import logger
from src.universal_regression.utils.common import get_size
from src.universal_regression.entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            # [NO-TOUCH ZONE]: Global SSL Bypass
            # WHY: Since urlretrieve doesn't take 'context', we set the 
            # default global context to unverified. 
            ssl._create_default_https_context = ssl._create_unverified_context
            
            # Now we call urlretrieve WITHOUT the context argument
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)