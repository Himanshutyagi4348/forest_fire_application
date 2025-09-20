Algerian Forest Fire FWI Prediction
Project Overview

This project predicts the Fire Weather Index (FWI) for Algerian forests using historical weather data. FWI helps authorities and environmental agencies assess fire risk and take preventive measures in real time.

The project features a Flask web application deployed on AWS, allowing users to interactively input weather parameters and get FWI predictions.

Features

Predict FWI: Input meteorological parameters like temperature, humidity, wind speed, and rainfall to get instant FWI predictions.

User-friendly Web Interface: Modern design with glassmorphism and fire-themed visuals.

Real-time Deployment: Hosted on AWS for 24/7 accessibility.

Folder Structure
forest-fire-fwi/
│
├─ application.py          # Flask app
├─ requirements.txt        # Python dependencies
├─ linreg.pkl              # Trained Linear Regression model
├─ scaler.pkl              # StandardScaler for feature scaling
├─ templates/              # HTML templates
│   ├─ index.html          # Home / Intro page
│   └─ Home.html           # Prediction page
├─ static/ (optional)      # CSS, JS, Images
├─ Procfile (optional)     # For AWS Elastic Beanstalk
└─ runtime.txt (optional)  # Python version for AWS

Tech Stack

Programming Language: Python

Web Framework: Flask

Data Handling: Pandas, NumPy

Machine Learning: Scikit-learn (Linear Regression, StandardScaler)

Frontend: HTML, CSS (Glassmorphism, Animated Effects)

Live Demo

Access the deployed application on AWS:
FWI Prediction Application


Installation & Local Setup

If you want to run the project locally:

Clone the repository
Deployment: AWS EC2 / Elastic Beanstalk
git clone https://github.com/Himanshutyagi4348/forest_fire_application/tree/main
cd forest-fire-fwi

Create a virtual environment
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
Install dependencies
python application.py

Usage

Open the home page (index.html).

Click Go to Prediction.

Enter all required input parameters.

Click Predict.

View the predicted FWI on the results section.

Data

The dataset contains the following features:

Feature	Description
Temperature	Daily temperature (°C)
RH	Relative Humidity (%)
Ws	Wind Speed (km/h)
Rain	Rainfall (mm)
FFMC	Fine Fuel Moisture Code
DMC	Duff Moisture Code
ISI	Initial Spread Index
Classes	Fire occurrence class
Region	Geographic region code
Model

Model: Linear Regression

Scaling: StandardScaler applied to all input features

Evaluation Metrics: RMSE, R²

Deployment

Hosted on AWS EC2 or Elastic Beanstalk.

Procfile (for Elastic Beanstalk) example:
web: gunicorn application:app
Python version can be specified in runtime.txt, e.g.:
python-3.12.0
Future Improvements

Integrate advanced ML models like Random Forest or XGBoost for better accuracy.

Add real-time weather API integration.

Include fire risk visualization maps.

Enhance mobile responsiveness and animations.

Authors

Himanshu Tyagi

License

This project is licensed under the MIT License.
