import os
import nltk

# Set the path to the directory containing the grammar file
dir_path = "my_grammar"

# Load the grammar from the file
file_path = os.path.join(dir_path, "my_grammar.cfg")
with open(file_path, "r") as f:
    grammar1 = nltk.CFG.fromstring(f.read())

    sent = ["Mary", "saw", "Bob"]
    rd_parser = nltk.RecursiveDescentParser(grammar1)
    for tree in rd_parser.parse(sent):
        print(tree)

