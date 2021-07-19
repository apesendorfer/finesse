import json
import ast
# import fasttext
# import numpy as np
from numpy.linalg import norm

# Import fasttext model
# model = fasttext.load_model("fasttext_model/cc.en.300.bin")

# Set of words from combined TF-IDF analysis results
with open('word_list.txt', 'r') as fle:
    data = fle.read()
words = data.split(", ")

json_word_list = json.dumps(words, indent = 4)
with open("word_list.json", "w") as outfile:
    outfile.write(json_word_list)

# Using code from https://www.kite.com/python/answers/how-to-read-a-dictionary-from-a-file-in--python
with open('pos_dict.txt', 'r') as fle:
    data = fle.read()
dictionary = ast.literal_eval(data)

json_dict = json.dumps(dictionary, indent = 4)
with open("part_of_speech_lookup.json", "w") as outfile:
    outfile.write(json_dict)

# # Numpy array to store word vectors
# arr = np.ndarray(shape=(29153, 300))
# # Store word vectors for the 29153 words in numpy array
# # Normalize all vectors when filling the array
# for i in range(0, 29153):
#     vec = model.get_word_vector(words[i])
#     arr[i] = np.array(vec)
#     arr[i] = arr[i] / norm(arr[i])

# json_fasttext_vecs = json.dumps(arr, indent = 4)
# with open("fasttext_vecs.json", "w") as outfile:
#     outfile.write(json_fasttext_vecs)

