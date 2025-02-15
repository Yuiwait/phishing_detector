from flask import Flask, request, jsonify
import joblib
from preprocess import clean_text

# Load the trained ML model and vectorizer
model = joblib.load("phishing_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Initialize Flask app
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "No email text provided"}), 400

    email_text = data["text"]
    return jsonify({"message": f"Received: {email_text}"})


if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
