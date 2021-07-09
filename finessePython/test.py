import numpy as np
import timeit
from main import Finesse

# Set of words from combined TF-IDF analysis results
f = open("word_list.txt", "r")
doc = f.read()
f.close()
words = doc.split(", ")

# Numpy array to store word vectors
arr = np.ndarray(shape=(29153, 300))

# Store word vectors for the 29153 words in numpy array
# Normalize all vectors when filling the array
for i in range(0, 29153):
    vec = model.get_word_vector(words[i])
    arr[i] = np.array(vec)
    arr[i] = arr[i] / norm(arr[i])

# IMPORT DICTIONARY FROM TEXT FILE

# Using code from https://www.kite.com/python/answers/how-to-read-a-dictionary-from-a-file-in--python

import ast

file = open("pos_dict.txt", "r")

contents = file.read()
dictionary = ast.literal_eval(contents)

file.close()

fin = Finesse(words, arr, dictionary)

print(fin.sentence_suggestions("What a wonderful day!"))
print("----------------\n")

start = timeit.default_timer()
print(fin.sentence_suggestions("Tokarczuk postulates the book’s ambiguous and fluid nature in the few first pages, developing a narrator with a yearning for the past, present, and future."))
stop = timeit.default_timer()
print('Time: ', stop - start)