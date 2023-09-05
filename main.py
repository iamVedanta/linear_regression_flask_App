import numpy as np
from flask import Flask,render_template, request
from sklearn.linear_model import LinearRegression


app = Flask(__name__)

if __name__=='__main__':
     app.run(debug=True)

@app.route('/')
def home():
    return render_template('index.html')

