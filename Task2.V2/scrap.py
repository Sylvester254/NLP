import json
import requests
from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from nltk.probability import FreqDist
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt')
nltk.download('stopwords')
"""
    This script handles the following tasks:
        Loads the urls from urls.json,
        scraps the contents of the urls, performs preprocessing on the text
        (Tokenize, Lowercase, Remove stop-words),
        Plot the frequency distribution of the words in the different documents,
        then saves the list of tokens as a slingle-line string.
"""

# Load URLs from JSON file
with open('urls.json', 'r') as f:
    urls = json.load(f)

for url in urls:
    # Extract the URL string from the dictionary using the "url" key
    url_string = url["url"]

    # Make the request and check object type
    r = requests.get(url_string)
    type(r)

    # Extract HTML from Response object and print
    html = r.text

    # Create a BeautifulSoup object from the HTML
    soup = BeautifulSoup(html, "html5lib")

    # Get soup title as string
    title = soup.title.string
    print(title)

    main_html = soup.find("div", {"id": "mw-content-text"})

    # Get the text out of the soup and print it
    text = main_html.get_text()

    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation and newlines
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\n', ' ', text)

    # Tokenize the text
    tokens = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    # Generate frequency distribution plot
    fdist = FreqDist(tokens)
    fdist.plot(30, cumulative=False)
    plt.show()

    # Convert the list of tokens to a string
    tokens_str = " ".join(tokens)

    # Save the processed data
    with open(f'corpus/{title.split(" - ")[0]}.txt', 'w') as f:
        f.write(tokens_str)
