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
        train_pipeline = TrainingPipeline()
        print("class instance")
        train_arr, test_arr,preprocessor_path = train_pipeline.run_pipeline()
        print("class method  successfully call")
        
        return jsonify({"message": "Pipeline executed successfully{train_arr.shape}{test_arr.shape}{preprocessor_path.shape}"})
    
    
    
    except Exception as e:
        CustomException(e,sys)
    
    

if __name__ == "__main__":   
    app.run(host="0.0.0.0",port=5000,debug=True)