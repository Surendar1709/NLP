import gensim 
from gensim.models import word2vec
import gensim.downloader as api

wv=api.load('word2vec-google-news-300')
vec_king=wv['king']
print(vec_king)


print()
print()
print(vec_king.shape)
vec_criket=wv['cricket']

print(vec_criket)

print(wv.most_similar('cricket'))
print(wv.most_similarity("hockey","sports"))


vec=wv['king']-wv['man']+wv['women']
print(wv.most_similar([vec])) 