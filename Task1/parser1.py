import os
import nltk

# Set the path to the directory containing the grammar file
dir_path = "my_grammar"

# Load the grammar from the file
file_path = os.path.join(dir_path, "my_grammar2.cfg")
with open(file_path, "r") as f:
    grammar2 = nltk.CFG.fromstring(f.read())

    sent = ["Mary", "saw", "Bob"]
    earley_parser = nltk.EarleyChartParser(grammar2)
    for tree in earley_parser.parse(sent):
        print(tree)

