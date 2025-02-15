import joblib
from preprocess import clean_text

# Load saved model and vectorizer
model = joblib.load("phishing_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")


def predict_email(text):
    """Predict if an email is phishing or safe."""
    cleaned_text = clean_text(text)  # Preprocess text
    X_test = vectorizer.transform([cleaned_text])  # Convert to vector
    prediction = model.predict(X_test)[0]  # Predict (0 = Safe, 1 = Phishing)

    return "Phishing" if prediction == 1 else "Safe"
