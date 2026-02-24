import os
import urllib.request as request
from src.datascience import logger
import zipfile
import os
from ensure import ensure_annotations
from pathlib import Path
from dataclasses import dataclass
from src.datascience.constants import *
from src.datascience.utils.common import *
from src.datascience.entity.config_entity import DataIngestionConfig
class DataIngestion  :  
    def __init__(self,config : DataIngestionConfig):
        self.config = config 
    
    def download_zip_file(self) : 
        if not os.path.exists(self.config.local_data_file) : 
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else : 
            print('File Exists')
            logger.info('File Already Exists.')


            
    def extract_zip_file(self) : 
        if os.path.exists(self.config.local_data_file) :
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path,exist_ok=True)
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
        else : 
            print('File Doesnt Exists')
            logger.info('File Doesnt Exists')