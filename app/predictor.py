import joblib
import pandas as pd

# Load saved files

model = joblib.load("model/customer_churn_model.pkl")
scaler = joblib.load("model/scaler.pkl")
model_columns = joblib.load("model/model_columns.pkl")

print(model_columns)
print("Churn_Yes" in model_columns)


def predict_churn(data: dict):
    """
    Takes customer data from the HTML form
    and returns prediction + probability.
    """

    # Create DataFrame
    df = pd.DataFrame([data])

    # One-Hot Encoding
    df = pd.get_dummies(df)

    # Match training columns
    df = df.reindex(columns=model_columns, fill_value=0)

    # Scale input
    df_scaled = scaler.transform(df)

    # Prediction
    prediction = model.predict(df_scaled)[0]

    # Probability of churn (class 1)
    churn_probability = model.predict_proba(df_scaled)[0][1] * 100

    if prediction == 1:
        result = "Customer is likely to Churn"
    else:
        result = "Customer is likely to Stay"

    return result, round(churn_probability, 2)
