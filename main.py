from src.datascience.config.configuration import Data_Config_Manager
from src.datascience.components.data_ingestion import DataIngestion

config_manager = Data_Config_Manager()
data_ingestion_config = config_manager.get_data_ingestion_config()

data_ingestion = DataIngestion(data_ingestion_config)

data_ingestion.download_zip_file()
data_ingestion.extract_zip_file()