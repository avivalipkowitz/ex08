# #!/usr/bin/env python



# def make_chains(corpus):
#     """Takes an input text as a string and returns a dictionary of
#     markov chains."""
#     return {}

# def make_text(chains):
#     """Takes a dictionary of markov chains and returns random text
#     based off an original text."""
#     return "Here's some random text."

# def main():
from sys import argv

input_file = argv[1]
myfile = open(input_file)

clean_text = ""

for line in myfile:
    line.rstrip()
    line = line.lower()
    for char in line:
        #convert each char to string, and then do ascii conv
        if ord(str(char)) ==10:
            char == " "
        elif ord(str(char)) >= 97 and ord(str(char)) <= 122:
            clean_text += char
        elif char == "":
            pass
        else:
            char = " "
            clean_text += char

word_list = clean_text.split(" ")


# monogram_count = {}
# for word in word_list:
#     if monogram_count.has_key(word):
#         monogram_count[word] += 1
#     else:
#         monogram_count.update({word:1})  #monogram_count[word] = 1
# del monogram_count['']
# print monogram_count
monogram = {}
for i in range(0, len(word_list)-1):
    if monogram.has_key(word_list[i]):  #check to see if monogram dict already has this key from word_list
        monogram[word_list[i]].append(word_list[i+1]) # if so, append the next word from word_list to monogram value
    else:
        value = [word_list[i + 1]]
        monogram.update({word_list[i]: value}) # if not, create new entry in dict
# del monogram['']

# bigram = {}
# for i in range(0, len(word_list)):
#     w1 = word_list[i]
#     w2 = word_list[i + 1]
#     w3 = word_list[i + 2]

#     bigram = (w1, w2)




    # Change this to read input_text from a file
    # input_text = "Some text"

    # chain_dict = make_chains(input_text)
    # random_text = make_text(chain_dict)
    # print random_text

# if __name__ == "__main__":
#     main()
