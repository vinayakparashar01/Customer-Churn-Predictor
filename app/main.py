from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from app.predictor import predict_churn

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")



@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.post("/predict")
def predict(
    request: Request,

    gender: str = Form(...),
    senior_citizen: str = Form(...),
    partner: str = Form(...),
    dependents: str = Form(...),
    tenure: int = Form(...),
    phone_service: str = Form(...),
    multiple_lines: str = Form(...),
    internet_service: str = Form(...),
    online_security: str = Form(...),
    online_backup: str = Form(...),
    device_protection: str = Form(...),
    tech_support: str = Form(...),
    streaming_tv: str = Form(...),
    streaming_movies: str = Form(...),
    contract: str = Form(...),
    paperless_billing: str = Form(...),
    payment_method: str = Form(...),
    monthly_charges: float = Form(...),
    total_charges: float = Form(...)
):

    customer_data = {
        "gender": gender,
        "SeniorCitizen": 1 if senior_citizen == "Yes" else 0,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }

    prediction, probability = predict_churn(customer_data)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "prediction": prediction,
            "probability": probability
        }
    )
