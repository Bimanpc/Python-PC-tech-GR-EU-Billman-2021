#!/usr/bin/python
 
words = {}
words["Hello"] = "Καλημέρα"
words["Yes"] = "Ναι"
words["No"] = "Οχι"
words["Bye"] = "Αντίο"
 
print(words)           # print key-pairs.
del words["Yes"]       # delete a key-pair.
print(words)           # print key-pairs.
words["Yes"] = "Ναι!"  # add new key-pair.
print(words)           # print key-pairs.
