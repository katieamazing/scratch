## # PYTHON 2 # ##
import nltk
import pronouncing
import random

from nltk.corpus import wordnet as wn
from nltk.corpus import webtext

def syn_to_word(part_of_speech):
    picked = str(random.choice(list(wn.all_synsets(part_of_speech))))
    return picked.split(".")[0].replace('_',' ')[8:]

def common(word):
    for fileid in webtext.fileids():
        if word in webtext.raw(fileid):
            print(word + " succeeded!")
            return True
    print(word + " failed for being uncommon.")
    return False

def random_noun():
    word = syn_to_word("n")
    while not common(word):
        word = syn_to_word("n")
    return word

def random_verb():
    word = syn_to_word("v")
    while " " in word or not common(word):
        word = syn_to_word("v")
    return word

def rhyme(word):
    l = pronouncing.rhymes(word)
    if not l:
        return word
    rhyme = random.choice(l)
    while not common(rhyme):
        rhyme = random.choice(l)
    return rhyme


def payload():
    I_nouns = ["I'm on the", "I've got this", "I have all this", "I'm made out of", "I'm under the", "I am mostly", "I wonder about", "I'm in love with"]
    b = random_noun()

    payload = \
        "She " + random_verb() + "s " + random_noun() + ",\n\
        I " + random_verb() + " " + b + ",\n\
        She's " + random_noun() + ",\n\
        " + random.choice(I_nouns) + " " + rhyme(b) + "."

    return payload

print(payload())
