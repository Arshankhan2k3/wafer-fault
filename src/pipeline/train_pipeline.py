import sys,os 
from src.exception import CustomException

#step 1
from src.components.data_ingestion import DataIngestion
#step 2 
from src.components.data_transformation import DataTransformation
#step 3
from src.components.model_trainer import ModelTrainer


class TrainingPipeline:
    
    def start_data_ingestion(self):
        try:
            data_ingestions = DataIngestion()
            feature_store_file_path = data_ingestions.initiate_data_ingestion()
            return feature_store_file_path
        
        except Exception as e:
            CustomException(e,sys)          
            
            
    def start_data_transformation(self, feature_store_file_path):
        try:
            data_transformation = DataTransformation(feature_store_file_path= feature_store_file_path)
            train_arr, test_arr,preprocessor_path = data_transformation.initiate_data_transformation()
            print("Shape of train_arr:", train_arr.shape)
            print("Shape of test_arr:", test_arr.shape)
            print(preprocessor_path)
            return train_arr, test_arr,preprocessor_path
            
        except Exception as e:
            raise CustomException(e,sys)            
        
       
    def start_model_training(self,train_arr,test_arr):
        try:
            model_trainer = ModelTrainer()
            model_score = model_trainer.initiate_model_trainer(train_arr,test_arr)
            return model_score
        
        except Exception as e:
            raise CustomException(e,sys)         
         
                
    
    def run_pipeline(self):
        try:
            feature_store_file_path = self.start_data_ingestion()
            train_arr, test_arr,preprocessor_path = self.start_data_transformation(feature_store_file_path)
            # print("Shape of train_arr:", train_arr.shape)
            # print("Shape of test_arr:", test_arr.shape)
            print(preprocessor_path)
            r2_square = self.start_model_training(train_arr, test_arr)
            print("training completed. Trained model score : ", r2_square)
            # return (train_arr, test_arr,preprocessor_path)
            

        except Exception as e: 
            raise CustomException(e, sys)

            
