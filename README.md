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

To run my application, open all the files in your IDE and make sure to import the following packages:
 - fastapi
 - uvicorn
 - joblib
 - pandas
 - scikit-learn
 - Jinja2
 - pymongo

To use my MongoDB Cluster, enter the password for my user 'vs7552', otherwise set up your own URI using the following instructions:
Setting up MongoDB URI:

Go to the MongoDB website and sign in to your MongoDB Atlas account (or sign up if you don't have one).
Create a new cluster or use an existing one.
Once your cluster is set up, navigate to the "Clusters" section and click on the "Connect" button for your cluster.
Choose "Connect your application" and copy the connection string (URI). It should look similar to this:
php
Copy code
mongodb+srv://<username>:<password>@<cluster-url>/<dbname>?retryWrites=true&w=majority
Replace <username>, <password>, <cluster-url>, and <dbname> with your actual MongoDB credentials and database name.

Use the FastAPI command to run the program:
uvicorn fast:app --reload
