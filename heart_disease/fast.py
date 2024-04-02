# Importing necessary libraries
from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
from pydantic import BaseModel
import joblib

# Creating FastAPI instance
app = FastAPI()
templates = Jinja2Templates(directory="templates")

# MongoDB setup
uri = "mongodb+srv://vs7552:<password>@heartdata.qs1nszn.mongodb.net/?retryWrites=true&w=majority&appName=heartdata"
client = MongoClient(uri)
db = client["heart_disease_db"]
collection = db["heart_disease_data"]

# Load trained model
model = joblib.load("heart_decision_tree_model.pkl")

# Pydantic model for input data
class InputData(BaseModel):
    age: int
    sex: int
    chest_pain_type: int
    resting_bp: int
    serum_cholesterol: int
    fasting_blood_sugar: int
    resting_ecg: int
    max_heart_rate: int
    exercise_angina: int
    oldpeak: float
    slope: int
    num_vessels: int
    thal: int

# Route to render the form
@app.get("/")
async def render_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

# Route to handle form submission
@app.post("/submit/")
async def submit_data(
    request: Request,
    age: int = Form(...),
    sex: str = Form(...),
    chest_pain_type: int = Form(...),
    resting_bp: int = Form(...),
    serum_cholesterol: int = Form(...),
    fasting_blood_sugar: int = Form(...),
    resting_ecg: int = Form(...),
    max_heart_rate: int = Form(...),
    exercise_angina: int = Form(...),
    oldpeak: float = Form(...),
    slope: int = Form(...),
    num_vessels: int = Form(...),
    thal: int = Form(...),
):
    # Store form data in MongoDB
    input_data = InputData(
        age=age,
        sex=sex,
        chest_pain_type=chest_pain_type,
        resting_bp=resting_bp,
        serum_cholesterol=serum_cholesterol,
        fasting_blood_sugar=fasting_blood_sugar,
        resting_ecg=resting_ecg,
        max_heart_rate=max_heart_rate,
        exercise_angina=exercise_angina,
        oldpeak=oldpeak,
        slope=slope,
        num_vessels=num_vessels,
        thal=thal,
    )
    inserted_data = collection.insert_one(input_data.dict())
    
    # Convert input data to a list of numerical values
    input_values = list(input_data.dict().values())

    # Make predictions
    target = model.predict([input_values])
    
    # Save prediction outcome back into the database
    collection.update_one({"_id": inserted_data.inserted_id}, {"$set": {"target": int(target[0])}})
    
    return templates.TemplateResponse(
        "confirmation.html", {"request": request, "inserted_id": str(inserted_data.inserted_id), "target": target[0]}
    )
