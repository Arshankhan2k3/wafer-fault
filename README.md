# Wafer Fault Prediction


## Overview

In the electronics industry, wafers are essential components for manufacturing integrated circuits and solar cells. They serve as the foundation for various microelectronic devices. Given their critical role, identifying faulty wafers is crucial to avoid disruptions and reduce costs in production processes.

This project aims to automate the detection of faulty wafers using machine learning, thereby reducing the need for manual inspection and minimizing operational interruptions.


## Project Structure

```plaintext
.
├── artifacts
│   ├── trained_model.pkl              # Saved model file after training
│   ├── evaluation_metrics.json        # Model performance metrics
│   ├── wafer_data.csv                 # Original wafer dataset in raw format
│
├── prediction_artifacts
│   ├── prediction_results.csv         # Results of predictions made on new data
│   ├── logs                           # Logs related to the prediction process
│
├── notebooks
│   ├── EDA.ipynb                      # Jupyter notebook for Exploratory Data Analysis (EDA)
│   ├── Model_Training.ipynb           # Jupyter notebook for model training and evaluation
│
├── src
│   ├── components
│   │   ├── data_ingestion.py          # Script for data extraction and loading
│   │   ├── data_preprocessing.py      # Script for data cleaning and transformation
│   │   ├── model_training.py          # Script for model training and validation
│   │
│   ├── pipelines
│   │   ├── training_pipeline.py       # Orchestrates the complete training process
│   │   ├── prediction_pipeline.py     # Handles the prediction process using the trained model
│
├── config
│   ├── config.yaml                    # Configuration file for project settings
│
├── templates
│   ├── index.html                     # HTML template for the Flask web interface
│   ├── results.html                   # HTML template to display prediction results
│
├── static
│   ├── styles
│   │   ├── style.css                  # CSS file for styling the web application
│   ├── scripts
│   │   ├── script.js                  # JavaScript file for adding interactive features to the web application
│
├── app.py                             # Flask application for deploying the model as a web service
├── setup.py                           # Script for setting up the project environment
├── requirements.txt                   # List of dependencies required to run the project
├── README.md                          # Project overview and instructions (this file)
└── venv/                              # Virtual environment directory for managing project dependencies


```
----
## Solution

The project uses a machine learning pipeline to process data fetched by the wafer sensors. The model predicts whether a wafer is faulty, automating the detection process and reducing reliance on manual labor.


## Running the Project

To run the project, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd wafer-fault-prediction
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Flask Application**:
   ```bash
   flask run
   ```

## Usage

- **Training Pipeline**: Automatically fetches data from MongoDB, trains the model, performs data ingestion, transformation, and hyperparameter tuning, and saves the best model.
- **Prediction Pipeline**: Allows users to upload a CSV file to predict the status of wafers as good or bad. The results are downloaded automatically.

## Dataset

The dataset contains sensor readings from various wafers, labeled as either faulty or non-faulty.

---

