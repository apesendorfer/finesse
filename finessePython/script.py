from finesse import Finesse
import numpy as np
from numpy.linalg import norm

def main(model):
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

    # IMPORT DICTIONARY FROM TEXT FILE
    # Using code from https://www.kite.com/python/answers/how-to-read-a-dictionary-from-a-file-in--python
    import ast
    with open('pos_dict.txt', 'r') as fle:
        contents = fle.read()
    dictionary = ast.literal_eval(contents)

    fin = Finesse(model, words, arr, dictionary)

