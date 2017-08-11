import nltk
import gensim

model = gensim.models.KeyedVectors.load_word2vec_format("C:\Users\KatieAmazing\Anaconda2\pretrained_model\GoogleNews-vectors-negative300.bin", binary=True)



w = "money"
print(w)
print(model.most_similar(w, topn=5))
