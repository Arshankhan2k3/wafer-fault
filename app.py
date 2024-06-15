import os,sys
from  flask import Flask, render_template, jsonify, request, send_file

from src.exception import CustomException
from src.logger import logging as lg

# step 1 [ Data Ingestion]
from src.pipeline.train_pipeline import TrainingPipeline

# from src.pipeline.predict_pipeline import PredictionPipeline

app = Flask(__name__)


@app.route("/")
def home():
    return "welcome to my application"

@app.route("/train")
def train_pipeline():
    try:
        train_pipelines = TrainingPipeline()
        
        file_path = train_pipelines.start_data_ingestion()
        print(f"Pipeline Result: {file_path}")
        return jsonify({'feature_store_file_path':(file_path)}) # Returning a valid JSON response
    
    except Exception as e:
        CustomException(e,sys)
    
    

if __name__ == "__main__":   
    app.run(host="0.0.0.0",port=5000,debug=True)