import os
import nltk
"""
This script creates the .cfg file for the grammar
"""
# Define the modified grammar
grammar2 = nltk.CFG.fromstring("""
S -> NP VP
NP -> Det N | Det Adj N | PN | NP Conj NP
VP -> V | V NP | VP Conj VP | V NP PP | Adv VP
PP -> P NP
Conj -> "and" | "or"
Det -> "a" | "an" | "the" | "my" | "The" 
Adj -> "very" | "perplexed" | "lazy"
N -> "man" | "dog" | "cat" | "telescope" | "park" | "sandwich" | "president" | "waiter" | "chair" | "table" | "chairs" | "tables" | "death"
V -> "saw" | "ate" | "walked" | "wanted" | "is" | "died" | "put" | "called" | "eating"
P -> "in" | "on" | "by" | "with"
PN -> "John" | "Mary" | "Bob" | "Oscar" | "Paris" | "Sally"
Adv -> "suddenly" | "quickly" | "slowly" | "very"
Copula -> "is"
""")

# Create a directory if it does not exist
dir_path = "my_grammar"
if not os.path.exists(dir_path):
    os.mkdir(dir_path)

# Save the grammar to a file in the directory
file_path = os.path.join(dir_path, "my_grammar2.cfg")
with open(file_path, "w") as f:
    f.write(str(grammar2))
