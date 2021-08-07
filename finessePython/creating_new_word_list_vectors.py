import numpy as np
from numpy.linalg import norm
import fasttext
import json

# Load new word set
new_word_list_file = "new_word_list.json"
with open(new_word_list_file, 'r') as f:
    new_word_list = json.load(f)

print("length of words: " + str(len(new_word_list)))
length = len(new_word_list)

model = fasttext.load_model("fasttext_model/cc.en.300.bin")

all_words_arr = np.ndarray(shape=(length, 300))
for i in range(0, length):
    vec = model.get_word_vector(new_word_list[i])
    all_words_arr[i] = np.array(vec)
    all_words_arr[i] = all_words_arr[i] / norm(all_words_arr[i])

with open('new_word_list_vectors.npy', 'wb') as f:
    np.save(f, all_words_arr)