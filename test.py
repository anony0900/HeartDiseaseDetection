from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np
import pickle

pred_args = [20,0,1,148,240,1,0,140,0,0,1]

model = pickle.load(open('NN_model.pkl','rb'))
scaler = joblib.load('scaler.pkl') 
preprocessed_data = scaler.transform([pred_args])
model_predcition = model.predict([preprocessed_data])
res = ""
if model_predcition[0][0] < model_predcition[0][1] :
    res = 'Affected'
else:
    res = 'Not affected'
print(model_predcition)
print(res)