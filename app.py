import os,sys
from  flask import Flask, render_template, jsonify, request, send_file

from src.exception import CustomException
from src.logger import logging as lg

# step 1 
from src.pipeline.train_pipeline import TrainingPipeline
# step 2
from src.pipeline.predict_pipeline import PredictionPipeline

app = Flask(__name__)


@app.route("/")
def home():
    return "welcome to my application"

@app.route("/train")
def train_pipeline():
    try:        
        train_pipeline = TrainingPipeline()
        print("class instance")
        train_pipeline.run_pipeline()
        return jsonify({"message": "Pipeline executed successfully"}), 200
    
    
    
    except Exception as e:
        CustomException(e,sys)

@app.route("/predict",methods = ['POST','GET'])
def upload():
    try:
        if request.method == 'POST':   
            prediction_pipeline = PredictionPipeline(request)
            prediction_file_detail=prediction_pipeline.run_pipeline()
            lg.info('prediction completed . Downloading prediction file')
            
            return send_file(prediction_file_detail.prediction_file_path,
                             download_name=prediction_file_detail.prediction_file_name,as_attachment= True)
        else:
            return render_template('upload_file.html')
    except Exception as e:
        raise CustomException(e,sys)
    

if __name__ == "__main__":   
    app.run(host="0.0.0.0",port=5000,debug=True)