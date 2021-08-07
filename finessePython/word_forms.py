from word_forms.word_forms import get_word_forms
import json

# Load 235892 word set
all_word_list_fle = "/Users/alex/Documents/GitHub/finesse/finessePython/total_word_list.json"
with open(all_word_list_fle, 'r') as f:
    all_words = json.load(f)

all_words = ["test", "experiment", "expect"]

new_list = []
count = 0

for word in all_words:
    word_forms = get_word_forms(word)
    set1 = word_forms["n"]
    set2 = word_forms["a"]
    set3 = word_forms["v"]
    set4 = word_forms["r"]
    combined_set = set.union(set1, set2, set3, set4)
    print(combined_set)
    new_list.extend(combined_set)
# print(new_list)

# new_list = set(new_list)
# new_list = sorted(new_list)
# new_word_list = json.dumps(new_list, indent = 4)
# with open("new_word_list.json", "w") as outfile:
#     outfile.write(new_word_list)