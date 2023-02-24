import os
import nltk

# Set the path to the directory containing the grammar file
dir_path = "my_grammar"

# Load the grammar from the file
file_path = os.path.join(dir_path, "my_grammar.cfg")
with open(file_path, "r") as f:
    grammar2 = nltk.CFG.fromstring(f.read())

    sent = ["Mary", "saw", "Bob"]
    rd_parser = nltk.RecursiveDescentParser(grammar2)
    for tree in rd_parser.parse(sent):
        print(tree)

    # i. Sally ate a sandwich.
    sent = "Sally ate a sandwich".split()
    rd_parser = nltk.RecursiveDescentParser(grammar2)
    for tree in rd_parser.parse(sent):
        print(tree)

    # ii. Sally and the president wanted and ate a sandwich.
    sent = "Sally and the president wanted and ate a sandwich".split()
    rd_parser = nltk.RecursiveDescentParser(grammar2)
    for tree in rd_parser.parse(sent):
        print(tree)


    # iii. the very very very perplexed president ate a sandwich.
    sent = "the very very very perplexed president ate a sandwich".split()
    rd_parser = nltk.RecursiveDescentParser(grammar2)
    for tree in rd_parser.parse(sent):
        print(tree)

    #iv. Sally is lazy
    sent = "Sally is lazy".split()
    rd_parser = nltk.RecursiveDescentParser(grammar2)
    for tree in rd_parser.parse(sent):
        print(tree)

    #v. Oscar died suddenly
    sent = "Oscar died suddenly".split()
    rd_parser = nltk.RecursiveDescentParser(grammar2)
    for tree in rd_parser.parse(sent):
        print(tree)

    #vi. The waiter put the chairs on the tables
    sent = "The waiter put the chairs on the tables".split()
    rd_parser = nltk.RecursiveDescentParser(grammar2)
    for tree in rd_parser.parse(sent):
        print(tree)

    #vii. Oscar called the waiter
    sent = "Oscar called the waiter".split()
    rd_parser = nltk.RecursiveDescentParser(grammar2)
    for tree in rd_parser.parse(sent):
        print(tree)

    #viii. Sally is eating a sandwich
    sent = "Sally is eating a sandwich".split()
    rd_parser = nltk.RecursiveDescentParser(grammar2)
    for tree in rd_parser.parse(sent):
        print(tree)
