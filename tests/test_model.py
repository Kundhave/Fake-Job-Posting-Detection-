import joblib

# Load trained model and vectorizer
tfidf_vectorizer = joblib.load('../models/tfidf_vectorizer.pkl')
xgb_model = joblib.load('../models/xgboost_model.pkl')

def predict_job_posting(text, model):
    # Vectorize the input
    text_vectorized = tfidf_vectorizer.transform([text])
    
    # Predict class
    prediction = model.predict(text_vectorized)[0]
    
    # Predict probabilities
    probas = model.predict_proba(text_vectorized)[0]
    
    label = 'Fake' if prediction == 1 else 'Real'
    print("\nPrediction:", label)
    print("Probability (Real): {:.4f}".format(probas[0]))
    print("Probability (Fake): {:.4f}".format(probas[1]))

job_text = """
URGENT HIRING!!! Work from Home Opportunity!

Earn $5,000/week with ZERO Experience Required!!!

We are seeking individuals to work from home doing simple tasks like data entry and email reading. No technical skills needed.

✅ Get paid instantly via PayPal or Bitcoin!
✅ Flexible hours, part-time or full-time!
✅ Limited slots available – ACT FAST!

To apply, send your name, address, and phone number to: workathomehr@gmail.com

Note: A one-time registration fee of $30 is required to process your application.

Apply NOW and change your life TODAY!
"""
print("\n--- Using XGBoost ---")
predict_job_posting(job_text, xgb_model)
