import sys,os 
from src.exception import CustomException

#step 1
from src.components.data_ingestion import DataIngestion



class TrainingPipeline:
    
    def start_data_ingestion(self):
        try:
            data_ingestions = DataIngestion()
            feature_store_file_path = data_ingestions.initiate_data_ingestion()
            return feature_store_file_path
        
        except Exception as e:
            CustomException(e,sys)          