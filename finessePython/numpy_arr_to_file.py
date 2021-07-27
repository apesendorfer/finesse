import numpy as np
from numpy.linalg import norm
import fasttext

model = fasttext.load_model("fasttext_model/cc.en.300.bin")

# Set of words from combined TF-IDF analysis results
with open('word_list.txt', 'r') as fle:
    data = fle.read()
words = data.split(", ")

# Create numpy array and store normalized word vectors
arr = np.ndarray(shape=(29153, 300))
for i in range(0, 29153):
    vec = model.get_word_vector(words[i])
    arr[i] = np.array(vec)
    arr[i] = arr[i] / norm(arr[i])

with open('tfidf_word_vectors.npy', 'wb') as f:
    np.save(f, arr)

with open('test.npy', 'rb') as f:
    a = np.load(f)

print(a[0])