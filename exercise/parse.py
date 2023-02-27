import os
import nltk

# Set the path to the directory containing the grammar file
dir_path = "my_grammar"

# Load the grammar from the file
file_path = os.path.join(dir_path, "my_grammar.cfg")
with open(file_path, "r") as f:
    grammar1 = nltk.CFG.fromstring(f.read())

    sent = ["Oscar", "died", "suddenly"]
    earley_parser = nltk.EarleyChartParser(grammar1)
    for tree in earley_parser.parse(sent):
        print(tree)
    
    sent = ["The", "waiter", "put", "the", "chairs", "on", "the", "tables"]
    earley_parser = nltk.EarleyChartParser(grammar1)
    for tree in earley_parser.parse(sent):
        print(tree)

    sent = ["Oscar", "called", "the", "waiter"]
    earley_parser = nltk.EarleyChartParser(grammar1)
    for tree in earley_parser.parse(sent):
        print(tree)

    sent = ["Oscar", "died", "in", "Paris"]
    earley_parser = nltk.EarleyChartParser(grammar1)
    for tree in earley_parser.parse(sent):
        print(tree)

    sent = ["Oscar", "died", "in", "a", "hotel", "in", "Paris"]
    earley_parser = nltk.EarleyChartParser(grammar1)
    for tree in earley_parser.parse(sent):
        print(tree)

    sent = ["The", "waiter", "came", "to", "the", "table", "when", "Oscar", "called", "him"]
    earley_parser = nltk.EarleyChartParser(grammar1)
    for tree in earley_parser.parse(sent):
        print(tree)

    sent = ["When", "Oscar", "called", "him", "the", "waiter", "came", "to", "the", "table"]
    earley_parser = nltk.EarleyChartParser(grammar1)
    for tree in earley_parser.parse(sent):
        print(tree)

    print("\n ********************************************************* \n ")

    sent = ["Oscar", "put"]
    earley_parser = nltk.EarleyChartParser(grammar1)
    for tree in earley_parser.parse(sent):
        print(tree)

    sent = ["The", "waiter", "saw", "on", "the", "tables"]
    earley_parser = nltk.EarleyChartParser(grammar1)
    for tree in earley_parser.parse(sent):
        print(tree)

    sent = ["The", "waiter", "put", "in", "the", "chairs"]
    earley_parser = nltk.EarleyChartParser(grammar1)
    for tree in earley_parser.parse(sent):
        print(tree)

    sent = ["The", "waiter", "put", "the", "chairs"]
    earley_parser = nltk.EarleyChartParser(grammar1)
    for tree in earley_parser.parse(sent):
        print(tree)
        
    sent = ["Oscar", "died", "the", "table"]
    earley_parser = nltk.EarleyChartParser(grammar1)
    for tree in earley_parser.parse(sent):
        print(tree)
        
    sent = ["When", "Oscar", "called", "him", "when", "the", "waiter", "came", "to", "the", "table"]
    earley_parser = nltk.EarleyChartParser(grammar1)
    for tree in earley_parser.parse(sent):
        print(tree)
