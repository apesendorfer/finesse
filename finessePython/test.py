with open('word_list.txt', 'r') as fle:
    data = fle.read()
words = data.split(", ")

print(words[0])