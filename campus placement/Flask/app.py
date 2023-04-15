# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 20:39:52 2022

@author: HI
"""

from flask import Flask, render_template, request
import pickle
import joblib

app = Flask(__name__)
model = pickle.load(open(r"C:\placement.pkl", 'rb'))


# ct=joblib.load('Placement')


@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/y_preict', methods=["post"])
def y_predict():
    x_test = [[(yo) for yo in request.form.values()]]
    prediction = model.predict(x_test)
    prediction = prediction[0]
    return render_template("secondpage.html", y=prediction)


if __name__ == '__main__':
    app.run(debug=True)
