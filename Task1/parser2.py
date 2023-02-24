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

    # i. Sally ate a sandwich.
    sent = ["Sally", "ate", "a", "sandwich"]
    earley_parser = nltk.EarleyChartParser(grammar2)
    for tree in earley_parser.parse(sent):
        print(tree)

    # ii. Sally and the president wanted and ate a sandwich.
    sent = ["Sally", "and", "the", "president", "wanted", "and", "ate", "a", "sandwich"]
    earley_parser = nltk.EarleyChartParser(grammar2)
    for tree in earley_parser.parse(sent):
        print(tree)

    # iii. the very very very perplexed president ate a sandwich.
    sent = ["the", "very", "very", "very", "perplexed", "president", "ate", "a", "sandwich"]
    earley_parser = nltk.EarleyChartParser(grammar2)
    for tree in earley_parser.parse(sent):
        print(tree)

    #iv. Sally is lazy
    sent = ["Sally", "is", "lazy"]
    earley_parser = nltk.EarleyChartParser(grammar2)
    for tree in earley_parser.parse(sent):
        print(tree)

    #v. Oscar died suddenly
    sent = ["Oscar", "died", "suddenly"]
    earley_parser = nltk.EarleyChartParser(grammar2)
    for tree in earley_parser.parse(sent):
        print(tree)

    #vi. The waiter put the chairs on the tables
    sent = ["The", "waiter", "put", "the", "chairs", "on", "the", "tables"]
    sent = [sent.lower() for sent in sent]
    earley_parser = nltk.EarleyChartParser(grammar2)
    for tree in earley_parser.parse(sent):
        print(tree)

    #vii. Oscar called the waiter
    sent = ["Oscar", "called", "the", "waiter"]
    earley_parser = nltk.EarleyChartParser(grammar2)
    for tree in earley_parser.parse(sent):
        print(tree)

    #viii. Sally is eating a sandwich
    sent = ["Sally", "is", "eating", "a", "sandwich"]
    earley_parser = nltk.EarleyChartParser(grammar2)
    for tree in earley_parser.parse(sent):
        print(tree)