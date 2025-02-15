import re
import nltk
from nltk.corpus import stopwords

# Download stopwords (run once)
nltk.download("stopwords")

# Load English stopwords
stop_words = set(stopwords.words("english"))

def clean_text(text):
    """
    Function to clean email text:
    - Removes URLs
    - Removes special characters
    - Removes stopwords
    - Converts text to lowercase
    """
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"\W", " ", text)  # Remove special characters
    text = " ".join([word.lower() for word in text.split() if word.lower() not in stop_words])
    return text
