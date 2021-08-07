import mlconjug3
import json

default_conjugator = mlconjug3.Conjugator(language='en')

# Load 235892 word set
all_word_list_fle = "total_word_list.json"
with open(all_word_list_fle, 'r') as f:
    all_words = json.load(f)

# all_words = ["test", "experiment", "expect"]

new_list = []
count = 0
for word in all_words:
    test_verb = default_conjugator.conjugate(word)
    all_conjugated_forms = test_verb.iterate()
    for form in all_conjugated_forms:
        try:
            if form[3] not in new_list:
                new_list.append(form[3])
                count += 1
                if count % 1000 == 0:
                    print(count)
        except:
            break
    #     new_list.append(form[3])

# print(new_list)

new_list = set(new_list)
new_list = sorted(new_list)
new_word_list = json.dumps(new_list, indent = 4)
with open("new_word_list.json", "w") as outfile:
    outfile.write(new_word_list)