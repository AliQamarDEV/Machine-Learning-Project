import os
from ensure import ensure_annotations
from pathlib import Path
from dataclasses import dataclass
from src.datascience.constants import *
from src.datascience.utils.common import *
from src.datascience.entity.config_entity import DataIngestionConfig

class Data_Config_Manager: 
    def __init__(self,config_filepath=CONFIG_FILE_PATH,
                 params_filepath = PARAMS_FILE_PATH,
                 schema_filepath = SCHEMA_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.param = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        create_directories([self.config.artifacts_root])
    def get_data_ingestion_config(self)->DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        obj = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        ) 
        return obj
