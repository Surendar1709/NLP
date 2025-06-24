from nltk.stem import PorterStemmer
from nltk.stem import RegexpStemmer
from nltk.stem import SnowballStemmer


'''
types pof  stemmer  
1 .porter stammer 
2 .regex stammer 
3 .snowball stammer 

  by  applyin  this   we  can the stem word  
'''
print("Normal Stammer ")

words = [
    'caresses', 'flies', 'dies', 'mules', 'denied',
    'died', 'agreed', 'owned', 'humbled', 'sized',
    'meeting', 'stating', 'siezing', 'itemization',
    'sensational', 'traditional', 'reference', 'colonizer',
    'plotted'
]

stemming=PorterStemmer()  # creating the  object 
for word in words:
    print(word+"----->"+stemming.stem(word))

print(stemming.stem("congratulation"))
print(stemming.stem("cooking"))

print(stemming.stem("sitting"))

print()

print("Regular expression Stemmer ")

print()
words = [
    'running', 'jumps', 'flies', 'agreed', 'humbled',
    'meeting', 'stating', 'siezing', 'itemization',
    'sensational', 'traditional', 'reference', 'colonizer',
    'plotted', 'advisable', 'computing', 'connected', 'connections'
]

#  to work with  regular expression required 
reg_stemmer=RegexpStemmer('ing$|s$|e$|able$',min=4)
for  word in words:
    print(word+"---->"+reg_stemmer.stem(word))

print("Snow ball stemmer")



# snow ball stemmer  is  best  from the all stemmer 
snow_ball=SnowballStemmer("english")
for word in words:
    print(word+"---->"+snow_ball.stem(word))



print()
print()

print("using the normal stammer ")
print(stemming.stem("fairly"),stemming.stem("Sportingly"))
print()

print("using the snownball stemmmer ")

print()
print(snow_ball.stem("Fairly"),snow_ball.stem("Spotingly"))

print(snow_ball.stem("Going"))
print(snow_ball.stem("curly"))



#    we dont  get  the  actuall meaning of some  word   in the  stemmming  so we  using the lammatization   