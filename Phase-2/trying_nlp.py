from operator import pos
import spacy
nlp = spacy.load("en_core_web_sm")

file = open("pseudocode.txt", "r")
text = file.readlines()
# print(text)
for line in text:
    line = line.strip()
    pos_tagged = nlp(line)
    for tag in pos_tagged:
        print(tag.text, tag.pos_, tag.dep_, end=" ")
    print()
