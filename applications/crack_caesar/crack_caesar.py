# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
import re

with open('ciphertext.txt') as f:
    words = f.read()

frequency_list = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

frequency_table = {}

def decrypt(text):
    # split text by word
    word_list = text.split()
    # create a list to hold each letter to decipher later
    letter_list = []

    # loop through each word:
    for word in word_list:
        # loop through each letter in each word:
        for letter in word:
            # if letter exists in the list, we can decode it
            if letter.upper() in frequency_list:
                # cache frequency if its there already or not
                if letter in frequency_table:
                    frequency_table[letter] += 1
                else:
                    frequency_table[letter] = 1
            # if not in our list add to master list of letters
            letter_list.append(letter)
        # if not last word, add a space
        if word != word_list[-1]:
            letter_list.append(" ")

    # sort items by most frequent
    items = list(frequency_table.items())
    items.sort(key=lambda x: -x[1])
    ordered_letters = list(dict(items).keys())

    decoded_list = []

    # loop through list of each letter
    for letter in letter_list:
        # if letter can be decrypted:
        if letter.upper() in frequency_list:
            # find the index of the letter, bc sorted by frequency, we can guess the index will match the correct letter
            index = ordered_letters.index(letter)
            # add decrypted letter to final list
            decoded_list.append(frequency_list[index])
        else:
            # if cant be decoded, put it in as is
            decoded_list.append(letter)
            
    # join final letters into a string
    final_decryption = "".join(decoded_list)

    return final_decryption

print(decrypt(words))

