from flask import Flask,render_template,request,jsonify
import pickle
import numpy as np
import pandas as pd
import joblib

app=Flask(__name__)
# regression=pickle.load(open('housing34.pkl','rb'))

@app.route("/")
def main():
    return render_template('frontend1.html')

@app.route('/predict',methods=['POST'])
def predict():
    area=float(request.form.get("area"))
    regression=pickle.load(open('./house.pkl','rb'))
    
    result=regression.predict(np.array([area]).reshape(1,1))
    print("area is {}".format(area))
    print(result)
    return render_template('frontend1.html',predict_price = "The price corresponding in INR is {}".format(result))
    
if __name__=='__main__':
    app.run(debug=True)