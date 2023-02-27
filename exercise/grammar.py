import os
import nltk

# Define the grammar
grammar1 = nltk.CFG.fromstring("""
  S -> NP VP
  NP ->  N | Det 
  NP ->  PN | N P PN | Det N Adv 
  VP -> V PP NP
  VP -> VP Adv
  VP -> V Adv
  VP -> P VP | V PP
  VP -> V Det N | Det N
  PP -> P NP | P
  Det -> "the" | "a" | "The"
  N -> "waiter" | "chairs" | "tables" | "hotel" | "manager" | "table"
  PN -> "Oscar" | "Paris" 
  V -> "died" | "put" | "saw" | "called" | "came"
  Adv -> "suddenly" | "quickly" | "slowly" | "when" | "him" | "When"
  P -> "in" | "on" | "to"
  """)

# Create a directory if it does not exist
dir_path = "my_grammar"
if not os.path.exists(dir_path):
    os.mkdir(dir_path)

# Save the grammar to a file in the directory
file_path = os.path.join(dir_path, "my_grammar.cfg")
with open(file_path, "w") as f:
    f.write(str(grammar1))