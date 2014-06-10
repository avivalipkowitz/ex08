#!/usr/bin/env python

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    return {}

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    return "Here's some random text."

def main():
    from sys import argv
    from random import randint

    input_file = argv[1]
    myfile = open(input_file)

    clean_text = myfile.read()
    clean_text = clean_text.lower()
    word_list = clean_text.split()

    monogram = {}
    for i in range(0, len(word_list)-1):
        if monogram.has_key(word_list[i]):  #check to see if monogram dict already has this key from word_list
            monogram[word_list[i]].append(word_list[i+1]) # if so, append the next word from word_list to monogram value
        else:
            value = [word_list[i + 1]]
            monogram.update({word_list[i]: value}) # if not, create new entry in dict

    bigram = {}

    for i in range(0, len(word_list) - 3):
        w1 = word_list[i]
        w2 = word_list[i + 1]
        w3 = word_list[i + 2]
        if not (w1, w2) in bigram:
            bigram[(w1, w2)] = [w3]
        else: 
            bigram[(w1,w2)].append(w3)


        
    monogram_key_list = monogram.keys()

    word_1_index = randint(0,len(monogram.keys()) - 1)
    rand_word_1 = monogram_key_list[word_1_index]

    word_2_list = monogram[rand_word_1]
    word_2_index = randint(0,len(word_2_list) - 1)
    rand_word_2 = word_2_list[word_2_index]

    crazy_text_list = [rand_word_1, rand_word_2]

    keep_adding = True
    crazy_text_list_index = 0

    while keep_adding:
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
                
    #    print crazy_text_list

    crazy_text = " ".join(crazy_text_list)
    print crazy_text

if __name__ == "__main__":
    main()
