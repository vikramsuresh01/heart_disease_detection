A user interactive project that predicts whether the patient has a heart disease or not.

The user entered the following parameters:

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Serum Cholesterol Level
- Fasting Blood Sugar
- Resting Electrocardiographic Results
- Maximum Heart Rate Achieved
- Exercise Induced Angina
- ST Depression Induced by Exercise Relative to Rest
- Slope of the Peak Exercise ST Segment
- Number of Major Vessels Colored by Flourosopy
- Thalassemia

The model used is a DecisionTreeClassifier as it is very effective in classification tasks, in this case, we classify whether or not the patient has a heart disease.<br />
The accuracy of the DecisionTreeClassifier model came to be: 0.9853658536585366<br />

The tech stack of the project includes the following components:

Frontend:

- HTML: Used for creating the structure and content of web pages.
- Jinja2Templates: Used for rendering HTML templates dynamically with data from the backend.

Backend:

- FastAPI: Used for building the backend web API.
- Python: Programming language used for backend development.
- Pydantic: Used for data validation and serialization/deserialization of data between the frontend and backend.
- MongoDB: NoSQL database used for persistently storing user data.
- scikit-learn: Library used for machine learning model training and prediction.
- Joblib: Used for saving and loading machine learning models.
- Pandas: Library used for data manipulation and analysis in Python.
