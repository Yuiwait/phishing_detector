import joblib
from preprocess import clean_text

# Load the trained model and vectorizer
model = joblib.load("phishing_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Example test email
email = "You have won a lottery! Click here to claim your prize."
cleaned_email = clean_text(email)

# Convert text to numerical features
X_test = vectorizer.transform([cleaned_email])

# Make prediction (1 = Phishing, 0 = Safe)
prediction = model.predict(X_test)[0]

print("Prediction:", "Phishing" if prediction == 1 else "Safe")
