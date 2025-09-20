from flask import Flask,request,jsonify,render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application=Flask(__name__)
app=application

#import linreg pickle and standard scaler pickle 
linreg_model=pickle.load(open('models/linreg.pkl','rb'))
standard_scalar=pickle.load(open('models/scaler.pkl','rb'))
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predict_data",methods=['GET','POST'])
def predict_datapoints():
    if request.method=="POST":
        Temperature=float(request.form.get('Temperature'))
        RH=float(request.form.get('RH'))
        Ws=float(request.form.get('Ws'))
        Rain=float(request.form.get('Rain'))
        FFMC=float(request.form.get('FFMC'))
        DMC=float(request.form.get('DMC'))
        ISI=float(request.form.get('ISI'))
        Classes=float(request.form.get('Classes')) 
        Region=float(request.form.get('Region'))

        new_data=standard_scalar.transform([[Temperature,
        RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])

        Result=linreg_model.predict(new_data)
        return render_template('Home.html',Result=Result[0])
    else:
        return render_template("Home.html")

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)