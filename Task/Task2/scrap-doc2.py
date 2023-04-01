import requests
from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from nltk.probability import FreqDist

nltk.download('punkt')
nltk.download('stopwords')


url = 'https://en.wikipedia.org/wiki/Mercedes-Benz'

# Make the request and check object type
r = requests.get(url)
type(r)
# Extract HTML from Response object and print
html = r.text
# print(html)

# Create a BeautifulSoup object from the HTML
soup = BeautifulSoup(html, "html5lib")
type(soup)
# Get soup title
soup.title

# Get soup title as string
soup.title.string

main_html = soup.find("div", {"id": "mw-content-text"})

# Get the text out of the soup and print it
text2 = main_html.get_text()
# print(text)


# ******************************Text Processing*****************************************

# Convert text to lowercase
text2 = text2.lower()
# print(text)

# Remove punctuation and newlines
text2 = re.sub(r'[^\w\s]', '', text2)
text2 = re.sub(r'\n', ' ', text2)

# Tokenize the text
tokens = word_tokenize(text2)
# print(tokens)

# Remove stopwords
stop_words = set(stopwords.words('english'))
tokens = [token for token in tokens if token not in stop_words]
# print(tokens)

fdist = FreqDist(tokens)
fdist.plot(30, cumulative=False)
plt.show()
# plt.savefig('freq-dist.png')

# Convert the list of tokens to a string
tokens_str = " ".join(tokens)

# Save the processed data
with open('corpus/document2.txt', 'w') as f:
    f.write(tokens_str)
