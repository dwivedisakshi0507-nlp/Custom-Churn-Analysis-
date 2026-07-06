# Custom-Churn-Analysis-
Predicting customer churn before it happens - because losing customers is expensive, and guessing isn't a strategy.
## Project Overview
Customer Churn Analysis is a Machine Learning project that predicts whether a customer is likely to churn based on customer information. The project features a Streamlit web application for making predictions and uses SQLite to store prediction records.

Live Demo

*Application:* https://customer-churn-analysis-by-sakshi.streamlit.app

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
The project uses the dataset:
- [WA_Fn-UseC_-Telco-Customer-Churn.csv](WA_Fn-UseC_-Telco-Customer-Churn.csv)

This dataset contains customer information used to train and evaluate the machine learning model.

## Installation

1. Install the required dependencies using the provided
   [requirements.txt](requirements.txt) file:

bash
pip install -r requirements.txt


2. Run the application using:

bash
streamlit run app.py


You can view the application code in [app.py](app.py).


## Database
The application uses *SQLite* for data storage. Prediction records are stored in the
[customers.db](customers.db) database.

## Machine Learning Model
The project uses a trained *Logistic Regression* model developed using *Scikit-learn*. The trained model is saved as
[churn_model.pkl](churn_model.pkl).

## Output
The application allows users to:

- Enter customer details
- Predict whether a customer is likely to churn
- Save prediction records in the SQLite database

## Author
"Sakshi Dwivedi"

GitHub: https://github.com/dwivedisakshi0507-nlp
