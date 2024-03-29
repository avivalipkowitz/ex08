#!/usr/bin/env python
from random import randint

def read_file():
    from sys import argv

    for i in range(1, len(argv)):
        input_file = argv[i]
        myfile = open(input_file)

        clean_text = myfile.read()
        clean_text = clean_text.lower()
        word_list = clean_text.split()

    return word_list

def create_monogram(word_list):

    monogram = {}
    for i in range(0, len(word_list)-1):
        if monogram.has_key(word_list[i]):  #check to see if monogram dict already has this key from word_list
            monogram[word_list[i]].append(word_list[i+1]) # if so, append the next word from word_list to monogram value
        else:
            value = [word_list[i + 1]]
            monogram.update({word_list[i]: value}) # if not, create new entry in dict

    return monogram

def create_bigram(word_list):

    bigram = {}

    for i in range(0, len(word_list) - 3):
        w1 = word_list[i]
        w2 = word_list[i + 1]
        w3 = word_list[i + 2]
        if not (w1, w2) in bigram:
            bigram[(w1, w2)] = [w3]
        else: 
            bigram[(w1,w2)].append(w3)
    return bigram

# def create_ngram(word_list,n):

#     n_gram = {}

#     for i in range(0, len(word_list)-(n+1)):
#         n_tuple_list = []
#         for j in range(0,(n+1)):
#             n_tuple_list.append(word_list[i+j])
#             n_tuple = tuple(n_tuple_list)
#             if not n_tuple in n_gram:
#                 n_gram[n_tuple] = word_list[i+n]
#             else:
#                 n_gram[n_tuple].append(word_list[i+n])
#     return n_gram

def make_text(word_list, monogram, bigram):
    monogram_key_list = monogram.keys()

    word_1_index = randint(0,len(monogram.keys()) - 1)
    rand_word_1 = monogram_key_list[word_1_index]

    word_2_list = monogram[rand_word_1]
    word_2_index = randint(0,len(word_2_list) - 1)
    rand_word_2 = word_2_list[word_2_index]

    crazy_text_list = [rand_word_1, rand_word_2]

    keep_adding = True
    crazy_text_list_index = 0

    while keep_adding and crazy_text_list_index < 500:
        w1 = crazy_text_list[crazy_text_list_index]
        w2 = crazy_text_list[crazy_text_list_index+1]
        bigram_pair = (w1,w2)

        if bigram_pair in bigram:
            word_3_index = randint(0, len(bigram[bigram_pair]) - 1)
            rand_word_3 = bigram[bigram_pair][word_3_index]
            crazy_text_list.append(rand_word_3)
            crazy_text_list_index += 1
        else:
            keep_adding = False

    crazy_text = " ".join(crazy_text_list)
    return crazy_text

def main():

    word_list = read_file()
    monogram = create_monogram(word_list)
    bigram = create_bigram(word_list)
    crazy_text = make_text(word_list, monogram, bigram)
    # n_gram = create_ngram(word_list,n)
    # crazy_text = make_text(word_list, monogram, n_gram)

    print crazy_text

if __name__ == "__main__":
    main()
