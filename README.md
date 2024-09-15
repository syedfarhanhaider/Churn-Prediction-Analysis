# Telecom Churn Analysis

## Project Overview
This project focuses on predicting customer churn for a telecom company. Using a machine learning model developed with Python and Scikit-Learn, we analyze customer behavior and predict churn likelihood with an accuracy of around 80%. The model has been deployed in a production-ready pipeline using Docker and AWS Elastic Beanstalk, streamlining the implementation for real-time use.

## Features
- **Model Accuracy**: Achieved an accuracy of about 80%.
- **Technologies**: Python, Scikit-Learn, Flask, Docker, AWS Elastic Beanstalk.
- **Deployment**: Model is deployed for real-time predictions using REST APIs.

## Files in the Repository
- `churn_data.csv`: The dataset used for training and testing the model.
- `churn_model.bin`: The saved machine learning model and DictVectorizer.
- `Churn_Prediction.ipynb`: Jupyter Notebook containing the end-to-end churn prediction analysis.
- `churn_prediction.py`: Python script used to preprocess data and build the churn prediction model.
- `predict.py`: REST API that receives customer data in JSON format and returns churn predictions.
- `predict-test.py`: Script for testing the REST API using sample customer data.
- `ping.py`: Health check endpoint to ensure the server is running.
- `customer.json`: Sample JSON file containing customer data for prediction.
- `Pipfile` and `Pipfile.lock`: Dependencies required for running the project.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/telecom-churn-analysis.git
  ```
2. Navigate to the project directory:
   ```bash
   cd telecom-churn-analysis
   ```
3. Install the necessary dependencies using pipenv:
   ```bash
   pipenv install
   ```
4. Run the Flask app:
   ```bash
   pipenv run python predict.py
   ```

## Usage
1. Ping the API to check if the server is running:
   ```bash
   curl http://localhost:9696/ping
   ```
   This should return pong.
2. Make a prediction: You can use the sample customer data (customer.json) to test the prediction API:
   ```bash
   curl -X POST http://localhost:9696/predict -H "Content-Type: application/json" -d @customer.json
   ```
3. Test the API: Run the predict-test.py script to send a test request to the API and print the results:
   ```bash
   pipenv run python predict-test.py
   ```

## Model Training
To retrain the model, follow the steps in Churn_Prediction.ipynb, which includes data preprocessing, model training, and evaluation. Once retrained, the model can be saved and deployed.

## Contributing
Feel free to fork this repository and contribute by submitting pull requests or suggesting new features. We welcome any suggestions to improve the project.
