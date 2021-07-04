
import fasttext

model = fasttext.load_model("/Users/alex/result/cc.en.300.bin")


## next steps?: preprocess recommendations on some 30k most common words

## long term goals: 1. bigrams, trigrams**, etc and 2. changing/allowing
## flexibility in tf/idf texts

# bigram example

## user text: going crazy
## suggestion: going like mad

# kerouac quote: "bop was going like mad all over America"


## **plagiarism becomes a bigger worry

class Finesse:

    #
    def __init__(self, words, arr):
        self.words = [] # list of words as strings
        self.arr = []   # list of vectors of words



    # user word

    def find_synonyms(self, word):

        synList = []



        results = {}

        # iterate through numpy array and find vectors that meet a threshold for cosine similarity
        cos_sim = 0.4
        for i in range(0, 29153):
            current = dot(user_word_vec, arr[i]) / (norm(user_word_vec) * norm(arr[i]))
            if current > cos_sim and words[i] != user_word and user_word[0:2] != words[i][0:2] and user_word[0:3] not in \
                    words[i]:
                results[words[i]] = current



        # dictionary: results
        sorted_values = sorted(results.values(), reverse=True)  # Sort the values
        sorted_dict = {}

        for i in sorted_values:
            for k in results.keys():
                if results[k] == i:
                    sorted_dict[k] = results[k]
                    break

        # print(sorted_dict)
        count = 0
        for key in sorted_dict:
            try:
                if input_sent_pos[word_index][1] in d[key]:
                    synList.append(key)
                    count += 1
                if count == 5:
                    break


        # print("---")

        return synList



    def sentence_suggestions(self, input_sent):
        parser = CoreNLPParser(url='http://localhost:9000')
        input_sent = parser.tokenize(input_sent)
        pos_tagger = CoreNLPParser(url='http://localhost:9000', tagtype='pos')
        input_sent_pos = list(pos_tagger.tag(input_sent))

        sent_length = len(input_sent_pos)

        output_list = []

        for word_index in range(len(sent_length)):


            user_word = input_sent_pos[word_index][0]
            # print("Word: " + user_word + " POS: " + input_sent_pos[word_index][1])

            user_word_vec = model.get_word_vector(user_word)

            output_list.append(find_synonyms(input_sent[word_index], user_word, user_word_vec))





