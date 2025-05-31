from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("model/model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    glucose = float(request.form["glucose"])
    bmi = float(request.form["bmi"])
    age = int(request.form["age"])
    features = np.array([[glucose, bmi, age]])
    prediction = model.predict(features)
    result = "Diabetic" if prediction[0] == 1 else "Not Diabetic"
    return render_template("index.html", prediction_text=f"Prediction: {result}")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)