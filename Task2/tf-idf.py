from sklearn.feature_extraction.text import TfidfVectorizer

# Load the text from the file
with open('document1.txt', 'r') as f:
    text = f.read()

# Create a TfidfVectorizer object
vectorizer = TfidfVectorizer()

# Calculate the tf-idf values
tf_idf = vectorizer.fit_transform([text])

# Print the feature names and their corresponding tf-idf values
feature_names = vectorizer.get_feature_names_out()
for col in tf_idf.nonzero()[1]:
    print(feature_names[col], ' - ', tf_idf[0, col])
