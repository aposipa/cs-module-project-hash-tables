# Your code here

import sys
import os
import re

robin_dict = {}

def printed_hash(n):
    return "#" * n

with open(os.path.join(sys.path[0], "robin.txt")) as r:
    for line in r:
        line = line.rstrip("\n").split(" ")
        for word in line:
            word = re.sub("[^a-zA-Z]+", "", word)
            word = word.lower()
            if word not in robin_dict:
                robin_dict[word] = 1
            
            else:
                robin_dict[word] += 1

    del robin_dict[""]

    robin_dict_items = list(robin_dict.items())
    robin_dict_items.sort(key=lambda x: (-x[1],) + x[:1])

    for i in robin_dict_items:
        print(f"{i[0]} \t {printed_hash(i[1])}".expandtabs(24))  