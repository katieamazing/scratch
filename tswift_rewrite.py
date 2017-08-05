import nltk
import pronouncing
import random

from nltk.corpus import wordnet as wn

def random_noun():
    picked = str(random.choice(list(wn.all_synsets("n"))))
    print(picked)
    return picked.split(".")[0].replace('_',' ')[8:]

def rhyme(word):
    l = pronouncing.rhymes(word)
    if not l:
        return word
    return random.choice(l)

def payload():
    b = random_noun()
    payload = \
        "She wears " + random_noun() + ",\n\
        I wear " + b + ",\n\
        She's " + random_noun() + ",\n\
        I'm on the " + rhyme(b) + "."
    return payload

print(payload())
