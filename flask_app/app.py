from flask import Flask, request, render_template
import joblib

app = Flask(__name__)
model = joblib.load("../models/xgboost_model.pkl")
vectorizer = joblib.load("../models/tfidf_vectorizer.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    description = request.form.get("description", "")
    
    if request.method == "POST":
        action = request.form.get("action", "predict")
        
        if action == "predict":
            description = request.form.get("description", "")
            if description:
                vectorized = vectorizer.transform([description])
                pred = model.predict(vectorized)[0]
                prediction = "Fake" if pred == 1 else "Real"
        elif action == "clear":
            description = ""
            prediction = None
    
    return render_template("index.html", prediction=prediction, description=description)

if __name__ == '__main__':
    app.run(debug=True)