from preprocess import clean_text

email = "Congratulations! You won a FREE iPhone. Click here: http://scam.com to claim your prize now!!!"
cleaned_email = clean_text(email)

print("Original Email:", email)
print("Cleaned Email:", cleaned_email)
