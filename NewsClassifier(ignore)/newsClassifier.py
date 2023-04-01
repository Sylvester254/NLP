import requests
import json
import json
import requests
from bs4 import BeautifulSoup

# Load URLs from JSON file
with open('urls.json', 'r') as f:
    urls = json.load(f)

for url in urls:
    url_string = url["url"]
    r = requests.get(url_string)

    if r.status_code == 200:
        soup = BeautifulSoup(r.content, "html.parser")
        article = soup.find("article")
        # Get the text out of the soup and print it
        content = article.get_text()
        # print(content)
        
        filename = url['title'] + '.txt'
        with open(filename, 'w') as f:
            f.write(content)
        print(f'Successfully saved {filename}')
    else:
        print(f"Error: {r.status_code}")
