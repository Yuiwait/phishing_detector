from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

# Secret key for JWT
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Rate Limiting Setup
limiter = Limiter(get_remote_address, app=app, default_limits=["5 per minute"])  # Default: 5 requests/min

# Authentication Middleware
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token or "Bearer " not in token:
            return jsonify({"message": "Token is missing or invalid!"}), 401

        try:
            token = token.split(" ")[1]  # Extract token part after "Bearer"
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token has expired!"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Invalid token!"}), 401

        return f(*args, **kwargs)

    return decorated
# Generate Token Route (Login Simulation)
@app.route("/login", methods=["POST"])
def login():
    auth = request.json  # Extract JSON body
    if not auth or auth.get("username") != "admin" or auth.get("password") != "password":
        return jsonify({"message": "Invalid credentials"}), 401  # Return 401 Unauthorized

    # Generate JWT token
    token = jwt.encode(
        {"user": auth["username"], "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
        app.config['SECRET_KEY'],
        algorithm="HS256"
    )
    return jsonify({"token": token})  # Return token as JSON response

# Phishing Detection Endpoint (Secured)
@app.route("/predict", methods=["POST"])
@limiter.limit("3 per minute")  # Limit this endpoint to 3 requests/minute per user
@token_required
def predict():
    return jsonify({"message": "Phishing prediction logic goes here!"})

if __name__ == "__main__":
    app.run(debug=True)
