import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# 🔹 Sample training data
X_train = ["You won a lottery!", "Click this link for a free gift", "Hello, how are you?", "Meeting at 5 PM"]
y_train = [1, 1, 0, 0]  # 1 = Phishing, 0 = Safe

# 🔹 Create the model pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", MultinomialNB())
])

# 🔹 Train the model
model.fit(X_train, y_train)

# 🔹 Save the trained model
joblib.dump(model, "phishing_model.pkl")

print("✅ Model saved successfully!")
