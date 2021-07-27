import numpy as np
from numpy.linalg import norm
import fasttext
from nltk.corpus import words
import json

words = words.words()
words = set(words)
words = sorted(words)
print("length of words: " + str(len(words)))

json_total_word_list = json.dumps(words, indent = 4)
with open("total_word_list.json", "w") as outfile:
    outfile.write(json_total_word_list)

model = fasttext.load_model("fasttext_model/cc.en.300.bin")

all_words_arr = np.ndarray(shape=(235892, 300))
for i in range(0, 235892):
    vec = model.get_word_vector(words[i])
    all_words_arr[i] = np.array(vec)
    all_words_arr[i] = all_words_arr[i] / norm(all_words_arr[i])

with open('all_word_vectors.npy', 'wb') as f:
    np.save(f, all_words_arr)