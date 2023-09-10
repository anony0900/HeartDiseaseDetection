from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('original.html')


@app.route("/predict", methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        Age = float(request.form['Age'])
        Sex = float(request.form['Sex'])
        ChestPainType = float(request.form['ChestPainType'])
        RestingBP = float(request.form['RestingBP'])
        Cholesterol = float(request.form['Cholesterol'])
        FastingBS= float(request.form['FastingBS'])
        RestingECG = float(request.form['RestingECG'])
        maxHR = float(request.form['maxHR'])
        ExerciseAngina = float(request.form['ExerciseAngina'])
        Oldpeak = float(request.form['Oldpeak'])
        ST_Slope = float(request.form['ST_Slope'])

        pred_args = [Age,Sex,ChestPainType,RestingBP,Cholesterol,FastingBS,RestingECG,maxHR,ExerciseAngina,Oldpeak,ST_Slope]
        # pred_args = [48,0,3,138,214,0,0,108,1,1.5,1]

        model = pickle.load(open('NN_model.pkl','rb'))
        scaler = joblib.load('scaler.pkl') 
        preprocessed_data = scaler.transform([pred_args])
        model_predcition = model.predict([preprocessed_data])
        res = ""
        if model_predcition[0][0] < model_predcition[0][1] :
            res = 'Affected'
        else:
            res = 'Not affected'
        
        if res == "Affected":
            return render_template('predict.html', prediction = res, prediction_color='red',confidence = model_predcition[0][1])
        else:
            return render_template('predict.html', prediction = res, prediction_color='green',confidence = model_predcition[0][0])

if __name__ == '__main__':
    app.run()
