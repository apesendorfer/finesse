import timeit
start = timeit.default_timer()
import config
stop = timeit.default_timer()
print('Import libraries: ', stop - start)
#import fasttext

import numpy as np

# cosine similarity of word vectors

from numpy import dot
from numpy.linalg import norm

from nltk.parse import CoreNLPParserg

# cos_sim = dot(a, b)/(norm(a)*norm(b))
model = config.model
#model = fasttext.load_model("/Users/alex/result/cc.en.300.bin")
# model = fasttext.load_model("/Users/benja/downloads/cc.en.300.bin.gz")


## next steps?: preprocess recommendations on some 30k most common words

## long term goals: 1. bigrams, trigrams**, etc and 2. changing/allowing
## flexibility in tf/idf texts

# bigram example

## user text: going crazy
## suggestion: going like mad

# kerouac quote: "bop was going like mad all over America"


## **plagiarism becomes a bigger worry

class Finesse:

    # Constructor
    def __init__(self, words, arr, d):
        self.words = words # list of words as strings
        self.arr = arr     # list of vectors of words
        self.d = d         # part of speech dictionary



    # user word


    # Takes as input a cosine similarity threshold, word vector, and word part of speech and returns up to 5 synonyms.
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
            # print(self.words[indices[i]])

            if count == 5 or full[indices[i]] < cos_sim:
                break

            try:
                # if user_word_pos in self.d[self.words[indices[i]]] and user_word != self.words[indices[i]] and user_word[0:3] not in self.words[indices[i]]:
                if user_word_pos in self.d[self.words[indices[i]]] and user_word[0:3] not in self.words[indices[i]]:
                     syn_list.append(self.words[indices[i]])
                     count += 1

            except:
                continue
            # in the future, to fix the broad except statement,
            # we may want to remove excess words from words[]

        return syn_list

    # Takes a string as input (a sentence), and returns a list of lists containing the synonym suggestions for each word in the original sentence.
    def sentence_suggestions(self, input_sent):
        parser = CoreNLPParser(url='http://localhost:9000')
        input_sent = parser.tokenize(input_sent)
        pos_tagger = CoreNLPParser(url='http://localhost:9000', tagtype='pos')
        input_sent_pos = list(pos_tagger.tag(input_sent))

        sent_length = len(input_sent_pos)

        output_list = []

        for word_index in range(sent_length):
            user_word = input_sent_pos[word_index][0]
            # print("Word: " + user_word + " POS: " + input_sent_pos[word_index][1])

            user_word_vec = model.get_word_vector(user_word)
            user_word_pos = input_sent_pos[word_index][1]

            output_list.append(self.find_synonyms(0.4, user_word, user_word_vec, user_word_pos))

        return output_list

start = timeit.default_timer()
# Set of words from combined TF-IDF analysis results
with open('word_list.txt', 'r') as fle:
    data = fle.read()
words = data.split(", ")
stop = timeit.default_timer()
print('Word List Time: ', stop - start)


start = timeit.default_timer()
# Numpy array to store word vectors
arr = np.ndarray(shape=(29153, 300))

# Store word vectors for the 29153 words in numpy array
# Normalize all vectors when filling the array
for i in range(0, 29153):
    vec = model.get_word_vector(words[i])
    arr[i] = np.array(vec)
    arr[i] = arr[i] / norm(arr[i])

stop = timeit.default_timer()
print('Vector Array Time: ', stop - start)

# with open('arr.txt', 'w') as file:
#     file.write(str(arr))

# IMPORT DICTIONARY FROM TEXT FILE

# Using code from https://www.kite.com/python/answers/how-to-read-a-dictionary-from-a-file-in--python

import ast
start = timeit.default_timer()
with open('pos_dict.txt', 'r') as fle:
    contents = fle.read()
dictionary = ast.literal_eval(contents)
stop = timeit.default_timer()
print('Dictionary Time: ', stop - start)

start = timeit.default_timer()
fin = Finesse(words, arr, dictionary)
stop = timeit.default_timer()
print('Instantiate Finesse Object: ', stop - start)

start = timeit.default_timer()
print(fin.sentence_suggestions("What a wonderful day!"))
stop = timeit.default_timer()
print('Short sentence suggestions: ', stop - start)

print("----------------\n")

start = timeit.default_timer()
print(fin.sentence_suggestions("Tokarczuk postulates the book’s ambiguous and fluid nature in the few first pages, developing a narrator with a yearning for the past, present, and future."))
stop = timeit.default_timer()
print('Long sentence suggestions: ', stop - start)