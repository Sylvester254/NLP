import os
import nltk

# Define the modified grammar
grammar2 = nltk.CFG.fromstring("""
  S -> NP VP
  VP -> V | V NP | V Adj | V NP Adj | V NP PP | V NP Adj PP
  PP -> P NP
  V -> "saw" | "ate" | "walked" | "is" | "eating" | V Conj
  Conj -> "and"
  PN -> "John" | "Mary" | "Bob" | "Oscar" | "Paris" | "Sally" | "president" | "waiter"
  NP -> NP Conj NP | Det N | Det Adj N | PN
  Det -> "a" | "an" | "the" | "my"
  Adj -> "very" | "perplexed" | "lazy"
  N -> "man" | "dog" | "cat" | "telescope" | "park" | "sandwich" | "chair" | "table"
  P -> "in" | "on" | "by" | "with"
  Adv -> "suddenly" | "quickly" | "slowly"
""")

# Create a directory if it does not exist
dir_path = "my_grammar"
if not os.path.exists(dir_path):
    os.mkdir(dir_path)

# Save the grammar to a file in the directory
file_path = os.path.join(dir_path, "my_grammar2.cfg")
with open(file_path, "w") as f:
    f.write(str(grammar2))
