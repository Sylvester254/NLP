# NATURAL LANGUAGE PROCESSING

## Task 1
```
grammar1 = nltk.CFG.fromstring("""
  S -> NP VP
  VP -> V NP | V NP PP
  PP -> P NP
  V -> "saw" | "ate" | "walked" | 
  V -> V NP | V NP PP | V Adv
  PN -> "John" | "Mary" | "Bob" | "Oscar" | "Paris"
  NP -> Det N | Det N PP
  Det -> "a" | "an" | "the" | "my"
  N -> "man" | "dog" | "cat" | "telescope" | "park"
  P -> "in" | "on" | "by" | "with"
  Adv -> "suddenly" | "quickly" | "slowly" |"very"
  """)
```

``` 
sent = "Mary saw Bob".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sent):
      print(tree)
(S (NP Mary) (VP (V saw) (NP Bob)))
```

Improve on the grammar above so that it correctly gives the parse tree for the below sentences. 
1. Sally ate a sandwich .
2. Sally and the president wanted and ate a sandwich .
3. the very very very perplexed president ate a sandwich .
4. Sally is lazy .
5. Oscar died suddenly.
6. The waiter put the chairs on the tables.
7. Oscar called the waiter.
8. Sally is eating a sandwich .

You can edit your grammar in a text file, say mygrammar.cfg. You can then load it into NLTK and parse with it as follows:

```
grammar1 = nltk.data.load('file:mygrammar.cfg')
sent = "Mary saw Bob".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sent):
      print(tree)
```

## Task 2

Choose several topics of your choice. Download different webpages that talk about the chosen topics (5 to 10 pages)
Download a webpage online using the sample code below 
Save each webpage as a separate file.

```
import requests# install this using:  pip install requests
from bs4 import BeautifulSoup # install this using: pip install bs4
url = 'https://www.gutenberg.org/files/2701/2701-h/2701-h.htm'
```

<b> Make the request and check object type</b>
```
r = requests.get(url)
type(r)
# Extract HTML from Response object and print
html = r.text
#print(html)
# Create a BeautifulSoup object from the HTML
soup = BeautifulSoup(html, "html5lib")
type(soup)
# Get soup title
soup.title
```

<b>Get soup title as string</b>

`soup.title.string`

<b>Get the text out of the soup and print it</b>
```
text = soup.get_text()
#print(text)
```

For each text perform
1. Tokenize
2. Lowercase
3. Remove stop-words
4. Plot the frequency distribution of the words in the different documents
5. Calculate the tf-idf for each document in your corpus
6. For each document, show the top 10 words with the highest tf.idf values
7. Use cosine similarity to find the most similar documents in your text. HINT create a matrix of similarities where each document is compared to every other sentence. Give the top 5 most similar documents in your corpus. You should see that documents that talk about the same topic are more similar to documents that talk about different topics.