import numpy as np
from flask import Flask,render_template, request
from sklearn.linear_model import LinearRegression


app = Flask(__name__)

if __name__=='__main__':
     app.run(debug=True)

@app.route('/',methods=['GET','POST'])
def answer():
    input_prediction = request.form.get('predict')




    X = np.array([1, 2, 3, 4, 5])  # Input feature (independent variable)
    y = np.array([1, 2, 3, 4, 5])  # Target variable (dependent variable)


    # Reshape X to a 2D array (required for sklearn)
    X = X.reshape(-1, 1)

    # Create a linear regression model
    model = LinearRegression()

    # Fit the model to the data
    model.fit(X, y)

    # Accept user input for prediction
    try:
        input_value = float(input_prediction)
        input_value = np.array([[input_value]])
        prediction = model.predict(input_value)
        print(f"Predicted output: {prediction[0]}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")



    return render_template("index.html", prediction=prediction[0])

