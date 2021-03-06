import fasttext
import numpy as np
from numpy.linalg import norm
import spacy
import json
import boto3
import os
import base64

ACCESS_KEY = os.environ["AWS_ACCESS_KEY_ID"]
SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]

def lambda_handler(event, context):
    BUCKET = "finesse-data"
    client = boto3.client(
        "s3", aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_ACCESS_KEY
    )
    # Load models
    # model = fasttext.load_model(client.get_object(Bucket=BUCKET, Key="cc.en.300.bin"))
    nlp = spacy.load("en_core_web_sm")
    
    # Load word list: set of words from combined TF-IDF analysis results
    word_list_fle = client.get_object(Bucket=BUCKET, Key="word_list.json")
    words = json.loads(word_list_fle.read().decode())

    # Create numpy array and store normalized word vectors
    # arr = np.ndarray(shape=(29153, 300))
    # for i in range(0, 29153):
    #     vec = model.get_word_vector(words[i])
    #     arr[i] = np.array(vec)
    #     arr[i] = arr[i] / norm(arr[i])
    tfidf_word_vectors_fle = client.get_object(Bucket=BUCKET, Key="tfidf_word_vectors.npy")
    with open(tfidf_word_vectors_fle, 'rb') as f:
        arr = np.load(f)

    # Load 235892 word set
    all_word_list_fle = client.get_object(Bucket=BUCKET, Key="total_word_list.json")
    all_words = json.loads(all_word_list_fle.read().decode())

    all_word_vectors_fle = client.get_object(Bucket=BUCKET, Key="all_word_vectors.npy")
    with open(all_word_vectors_fle, 'rb') as f:
        all_vecs = np.load(f)

    dict_fle = client.get_object(Bucket=BUCKET, Key="part_of_speech_lookup.json")
    dictionary = json.loads(dict_fle.read().decode())

    # Takes a string as input (a sentence), and returns a list of lists containing the synonym suggestions for each word in the original sentence.
    input_sent = event["text"]
    doc = nlp(input_sent)
    input_sent = []
    input_sent_pos = []
    COS_SIM = 0.4
    for token in doc:
        input_sent.append(token.text)
        input_sent_pos.append(token.tag_)
    output_list = []
    for word_index in range(len(input_sent)):
        # Find index of word in all_words list
        if input_sent[word_index] in all_words or input_sent[word_index].lower() in all_words:
            try:
                all_words_index = all_words.index(input_sent[word_index])
            except:
                all_words_index = all_words.index(input_sent[word_index].lower())
            user_word = input_sent[word_index].lower()
            # Retrieve corresponding word vector from all_vecs nparray
            user_word_vec = all_vecs[all_words_index]
            # user_word_vec = model.get_word_vector(user_word)
            user_word_pos = input_sent_pos[word_index]
            syn_list = []
            current = user_word_vec / norm(user_word_vec)
            # code from https://stackoverflow.com/questions/20825990/find-multiple-maximum-values-in-a-2d-array-fast
            # for finding the num_largest maxima in a numpy array
            num_largest = 15
            full = np.dot(arr, current)
            indices = full.argpartition(full.size - num_largest, axis=None)[-num_largest:]
            count = 0
            for i in range(num_largest-1, -1, -1):
                if count == 5 or full[indices[i]] < COS_SIM:
                    break
                try:
                    if user_word_pos in dictionary[words[indices[i]]] and user_word[0:3] not in words[indices[i]]:
                        syn_list.append(words[indices[i]])
                        count += 1
                except:
                    continue

            output_list.append(syn_list)
        else:
            output_list.append([])

    origin = event['headers']['origin']

    if origin == 'https://apesendorfer.github.io':
        response = {
            "statusCode": 200,
            "input_list": json.dumps(input_sent),
            "output_list": json.dumps(output_list),
            'headers': {
                'Access-Control-Allow-Origin': origin,
                # 'Access-Control-Allow-Credentials' : True,
            },
        }
        return response
    else:
        response = {
            "statusCode": 500,
        }
        return response
    