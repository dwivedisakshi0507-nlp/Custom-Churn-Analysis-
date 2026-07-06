import streamlit as st
import joblib
import sqlite3
conn = sqlite3.connect("customers.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    prediction TEXT
)
""")
conn.commit()
st.set_page_config(page_title="Telco Customer Churn Prediction")

st.title("Telco Customer Churn Prediction")

model = joblib.load("churn_model.pkl")

st.success("Model Loaded Successfully!")
customer_name = st.text_input("Customer Name")
tenure = st.number_input("Tenure (Months)", min_value=0)

monthly_charges = st.number_input("Monthly Charges", min_value=0.0)

total_charges = st.number_input("Total Charges", min_value=0.0)
if st.button("Predict"):
    input_data = [[tenure, monthly_charges, total_charges]]

    prediction = model.predict(input_data)

    result = "Churn" if prediction[0] == 1 else "No Churn"

    st.success(result)

    cursor.execute(
        "INSERT INTO predictions (customer_name, prediction) VALUES (?, ?)",
        (customer_name, result)
    )

    conn.commit()
    conn.close()
st.write(" Congratulations! Your Streamlit app is running.")