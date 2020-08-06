import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here

def words_table(text):
    words_list = text.split()

    cache = {}

    for i in range(len(words_list)-1):
        if words_list[i] in cache:
            cache[words_list[i]].append(words_list[i + 1])
        else:
            cache[words_list[i]] = [words_list[i + 1]]
    
    cache[words_list[-1]] = []

    return cache

# TODO: construct 5 random sentences
# Your code here

def random_sentences(text):
    cache = words_table(text)
    random_word = random.choice(text.split())

    stop_conditions = ['.','?','!','."','?"','!"']

    current_words = cache[random_word]

    current_random = random.choice(current_words)

    sentence = random_word

    while current_random[-1] not in stop_conditions and current_random[-2:] + current_random[-1] not in stop_conditions and len(cache[current_random]) > 1:
        if cache[current_random] != [] and cache[current_random] != None:
            sentence = sentence + " " + current_random
            current_random = random.choice(cache[current_random])

        else:
            current_random = random.choice(current_words)

    sentence += " "+ current_random
    print("Sentence: ", sentence)

random_sentences(words)
random_sentences(words)
random_sentences(words)
random_sentences(words)
random_sentences(words)

