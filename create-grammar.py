import os
import nltk

# Define the grammar
grammar1 = nltk.CFG.fromstring("""
  S -> NP VP
  VP -> V NP | V NP PP
  PP -> P NP
  V -> "saw" | "ate" | "walked" 
  V -> V NP | V NP PP | V Adv
  PN -> "John" | "Mary" | "Bob" | "Oscar" | "Paris"
  NP -> Det N | Det N PP
  Det -> "a" | "an" | "the" | "my"
  N -> "man" | "dog" | "cat" | "telescope" | "park"
  P -> "in" | "on" | "by" | "with"
  Adv -> "suddenly" | "quickly" | "slowly" | "very"
  """)

# Create a directory if it does not exist
dir_path = "my_grammar"
if not os.path.exists(dir_path):
    os.mkdir(dir_path)

# Save the grammar to a file in the directory
file_path = os.path.join(dir_path, "my_grammar.cfg")
with open(file_path, "w") as f:
    f.write(str(grammar1))
