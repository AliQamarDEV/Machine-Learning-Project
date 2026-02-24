from src.datascience.config.configuration import Data_Config_Manager
from src.datascience.components.data_ingestion import DataIngestion
from src.datascience.utils import *


STAGE_NAME = 'Data Ingestion Stage'

class DataIngestionTrainingPipeline :    
    def _init_(self) : 
        pass
    def initiate_data_ingestion(self) :
        config_manager = Data_Config_Manager()
        data_ingestion_config = config_manager.get_data_ingestion_config()

        data_ingestion = DataIngestion(data_ingestion_config)

        data_ingestion.download_zip_file()
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e