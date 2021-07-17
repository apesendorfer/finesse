import spacy
from spacy.lang.en.examples import sentences 
import time


start = time.time()

nlp = spacy.load("en_core_web_lg")

end = time.time()
print(end - start)
doc = nlp("This, is a test sentence.")
for token in doc:
    print(token.text, token.tag_, token.vector)