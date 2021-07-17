import fasttext
import numpy as np
from numpy.linalg import norm
import spacy

# model = fasttext.load_model("fasttext_model/cc.en.300.bin")
nlp = spacy.load("en_core_web_lg") # or load en_core_web_sm for greater efficiency

class Finesse:
    # Constructor
    def __init__(self, words, arr, d):
        self.words = words # list of words as strings
        self.arr = arr     # list of vectors of words
        self.d = d         # part of speech dictionary

    # Takes as input a cosine similarity threshold, word, word vector, and word part of speech and returns up to 5 synonyms.
    def find_synonyms(self, cos_sim, user_word, user_word_vec, user_word_pos):
        # cos_sim should be 0.4 for this normalization method
        syn_list = []
        current = user_word_vec / norm(user_word_vec)
        # code from https://stackoverflow.com/questions/20825990/find-multiple-maximum-values-in-a-2d-array-fast
        # for finding the num_largest maxima in a numpy array
        num_largest = 15
        full = np.dot(self.arr, current)
        indices = full.argpartition(full.size - num_largest, axis=None)[-num_largest:]
        count = 0
        for i in range(num_largest-1, -1, -1):
            if count == 5 or full[indices[i]] < cos_sim:
                break
            try:
                if user_word_pos in self.d[self.words[indices[i]]] and user_word[0:3] not in self.words[indices[i]]:
                     syn_list.append(self.words[indices[i]])
                     count += 1
            except:
                continue
            # in the future, to fix the broad except statement,
            # we may want to remove excess words from words[]
        return syn_list

    # Takes a string as input (a sentence), and returns a list of lists containing the synonym suggestions for each word in the original sentence.
    def sentence_suggestions(self, input_sent: str) -> list:
        doc = nlp(input_sent)
        input_sent = []
        input_sent_pos = []
        for token in doc:
            input_sent.append(token.text)
            input_sent_pos.append(token.tag_)
        output_list = []
        for word_index in range(len(input_sent)):
            user_word = input_sent[word_index].lower()
            user_word_vec = doc[word_index].vector
            #user_word_vec = model.get_word_vector(user_word)
            user_word_pos = input_sent_pos[word_index]
            output_list.append(self.find_synonyms(0.4, user_word, user_word_vec, user_word_pos))
        return output_list

# Set of words from combined TF-IDF analysis results
with open('word_list.txt', 'r') as fle:
    data = fle.read()
words = data.split(", ")

# Numpy array to store word vectors
arr = np.ndarray(shape=(29153, 300))
# Store word vectors for the 29153 words in numpy array
# Normalize all vectors when filling the array
for i in range(0, 29153):
    vec = model.get_word_vector(words[i])
    arr[i] = np.array(vec)
    arr[i] = arr[i] / norm(arr[i])


# Using code from https://www.kite.com/python/answers/how-to-read-a-dictionary-from-a-file-in--python
import ast
with open('pos_dict.txt', 'r') as fle:
    data = fle.read()
dictionary = ast.literal_eval(data)

fin = Finesse(words, arr, dictionary)

# print(fin.sentence_suggestions("What a wonderful day!"))
# print("----------------\n")

#print(fin.sentence_suggestions("Tokarczuk postulates the book’s ambiguous and fluid nature in the few first pages, developing a narrator with a yearning for the past, present, and future."))
print(fin.sentence_suggestions(str(input("Enter your sentence: "))))
while(str(input("Continue: Y/N: ")) == "Y"):
    print(fin.sentence_suggestions(str(input("Enter your sentence: "))))