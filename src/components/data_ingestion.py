import os,sys
import numpy as np
import pandas as pd

from pymongo import MongoClient
from zipfile import Path
from src.constant import *
from src.exception import CustomException
from src.logger import logging
from src.utils.main_utlis import MainUtlis
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    artifact_folder:str = os.path.join(artifact_folder)
    
class DataIngestion:
    def __init__(self) -> None:
        self.data_ingestion_config = DataIngestionConfig()
        self.utils = MainUtlis()
        
    def export_collection_as_dataframe(self,collection_name, db_name):
        try:
            
            mongo_client = MongoClient(MONGO_DB_URL)
            collection = mongo_client[db_name][collection_name]

            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)
            df.replace({"na": np.nan}, inplace=True)

            return df

        except Exception as e:
            raise CustomException(e, sys)
        
    def export_data_into_feature_store_file_path(self)-> pd.DataFrame:
        """_summary_
        Method Name : export_data_into_features_store_file_path
        Description : This method reads data from mongodb and saves it into artifacts.
        
        Output      : dataset is returned as a pd.DataFrame
        On Failure  : write an exception log and then raise an exception         """
        
        try:
            logging.info(f"Exporting data from mongodb")
            raw_file_path = self.data_ingestion_config.artifact_folder
            os.makedirs(raw_file_path,exist_ok=True)
            print('step 1')
            sensor_data = self.export_collection_as_dataframe(
                collection_name=MONGO_COLLECTION_NAME,
                db_name= MONGO_DATABASE_NAME            )
            print("step 2")
            feature_store_file_path = os.path.join(raw_file_path,'wafer_fault.csv')
            sensor_data.to_csv(feature_store_file_path,index=False)
            logging.info(f'saving exported data into features store file path:{raw_file_path}')
            return feature_store_file_path
        
        except Exception as e:
            raise CustomException(e,sys)
    
    def initiate_data_ingestion(self) -> Path:
        """
            Method Name : initiate_data_ingestion
            Description : This method initiates the data ingestion components of training pipeline
            
            Output      : train set and test set are returned as the  artifacts of data ingestion components
            On Failure  : Write an exception log and then rasie an exception
            
            version     : 0.0.1
            Revisions   : moved setup on cloud
        """
        logging.info("Entered initiate_data_ingestion method of Data_ingestion class")
        try:
            feature_store_file_path = self.export_data_into_feature_store_file_path()
            logging.info("Got the data from Mongodb")
            logging.info("Exited initiate_data_ingestion method of Data_ingestion class")
            
            return feature_store_file_path
        
        except Exception as e:
            CustomException(e,sys) 
                    
        