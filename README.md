# Custom-Churn-Analysis-
Predicting customer churn before it happens - because losing customers is expensive, and guessing isn't a strategy.
## Project Overview
Customer Churn Analysis is a Machine Learning project that predicts whether a customer is likely to churn based on customer information. The project features a Streamlit web application for making predictions and uses SQLite to store prediction records.

## Features
- Predict customer churn using a trained Machine Learning model
- Interactive Streamlit web application
- Store prediction records in an SQLite database
- Simple and user-friendly interface

## Technologies Used
- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- SQLite
- Joblib

## Project Structure
```
Customer-Churn-Analysis/
│── app.py
│── Customer_Churn_Analysis.ipynb
│── churn_model.pkl
│── customers.db
│── requirements.txt
│── WA_Fn-UseC_-Telco-Customer-Churn.csv
│── README.md
```

## Dataset
The project uses the *WA_Fn-UseC_-Telco-Customer-Churn.csv* dataset to train and evaluate the machine learning model.

## Installation
1. Download or clone this repository.
2. Install the required dependencies:

bash
pip install -r requirements.txt


3. Run the Streamlit application:

bash
streamlit run app.py


## Database
The project uses *SQLite* (customers.db) to store customer prediction records.

## Machine Learning Model
- Framework: Scikit-learn
- Model File: churn_model.pkl

## Output
The application allows users to:

- Enter customer details
- Predict whether a customer is likely to churn
- Save prediction records in the SQLite database

## Author
"Sakshi Dwivedi"

GitHub: https://github.com/dwivedisakshi0507-nlp
