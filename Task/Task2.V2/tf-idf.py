import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
"""
    This script handles the following tasks:
        Calculate the tf-idf for each document in your corpus
        For each document, show the top 10 words with the highest tf.idf values
        Find the most similar documents in your text.
"""
# Initialize vectorizer
vectorizer = TfidfVectorizer(input='filename')

# Get the paths of the preprocessed text files in the corpus directory
corpus_path = 'corpus/'
corpus_files = [os.path.join(corpus_path, f) for f in os.listdir(corpus_path)]

# Calculate the TF-IDF for each document in the corpus
tfidf_matrix = vectorizer.fit_transform(corpus_files)

# Convert the sparse matrix to a dense matrix
dense_matrix = tfidf_matrix.toarray()

# Print the dense matrix
print(dense_matrix)

# Get the feature names (i.e., the unique terms in the corpus)
feature_names = vectorizer.get_feature_names_out()

# Print the top 10 terms with the highest TF-IDF value for each document
for i in range(len(corpus_files)):
    print(f"Top 10 terms for document {i+1}:")
    doc_tfidf = tfidf_matrix[i]
    sorted_indices = doc_tfidf.toarray()[0].argsort()[::-1]
    for j in sorted_indices[:10]:
        print(f"\t{feature_names[j]}: {doc_tfidf.toarray()[0][j]:.2f}")


# Compute the cosine similarity matrix
similarity_matrix = cosine_similarity(tfidf_matrix)

# Find the top k most similar documents for each document
k = 5
for i in range(len(corpus_files)):
    print(f"Top {k} similar documents for {os.path.basename(corpus_files[i])}:")
    similarities = similarity_matrix[i]
    # Sort the similarities in descending order and get the top k indices
    top_k_indices = similarities.argsort()[::-1][1:k+1] 
    # Print the document names and similarity scores for the top k indices
    for j in top_k_indices:
        print(f"\t{os.path.basename(corpus_files[j])}:\tScore: {similarities[j]:.2f}")