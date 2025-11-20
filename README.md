# Telecom Customer Churn Prediction

A Flask web application that predicts customer churn using machine learning models trained on telecom customer data.

## Features

- Interactive web interface for customer data input
- Dual prediction models: Random Forest and Decision Tree
- Real-time churn prediction based on 19 customer attributes
- Clean, responsive UI design

## Models

The application uses two pre-trained machine learning models:
- **Random Forest** (`random_forest_model.pkl`)
- **Decision Tree** (`decision_tree_model.pkl`)

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   cd telco-churn
   python app.py
   ```

3. Open your browser and navigate to `http://localhost:5000`

## Input Features

The model predicts churn based on customer attributes including:
- Demographics (age, gender, dependents)
- Services (phone, internet, streaming)
- Account info (tenure, charges, contract type)
- Payment details

## Usage

1. Fill in the customer information form
2. Click predict to get churn probability
3. View results from both ML models

## Technologies

- **Backend**: Flask, Python
- **ML Libraries**: scikit-learn, pandas
- **Frontend**: HTML, CSS
- **Models**: Pickle serialized ML models

