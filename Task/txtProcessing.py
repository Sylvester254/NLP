import requests
from bs4 import BeautifulSoup

url = 'https://www.gutenberg.org/files/2701/2701-h/2701-h.htm#link2HCH0042'

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

# Get the text out of the soup and print it
text = soup.get_text()
# print(text)