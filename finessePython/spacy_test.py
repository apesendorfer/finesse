import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("I am happy.")
# All strings mapped to integers, for easy export to numpy


# for token in doc:
#     print(token.text, token.tag_, token.is_stop)


tokenized = []
parts_of_speech = []
for token in doc:
    tokenized.append(token.text.lower())
    parts_of_speech.append(token.tag_)

print(tokenized)
print(parts_of_speech)

