from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np
import pickle

pred_args = [48,0,3,138,214,0,0,108,1,1.5,1]

model = pickle.load(open('model.pkl','rb'))

model_predcition = model.predict([pred_args])
res = ""
if model_predcition[0][0] <= model_predcition[0][1] :
    res = 'Affected'
else:
    res = 'Not affected'

print(res)