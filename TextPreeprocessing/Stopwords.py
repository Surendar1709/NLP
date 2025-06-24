from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import nltk 
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer

from nltk.stem  import PorterStemmer
# stop  words are the  words   which  is   no0t provideing the  so much meaning  

snowball=SnowballStemmer('english')

lammatizer=WordNetLemmatizer() # crating the  word net  lammatizer 
nltk.download('stopwords')
print("------ stop Word in english --------")
print(stopwords.words('english'))
print(stopwords.words('tamil'))
 

str="""I have three visions for India. In 3000 years of our history, people from all over the world have come and invaded us, captured our lands, conquered our minds.

Yet we have not done this to any other nation. We have not conquered anyone.
We have not grabbed their land, their culture, their history, and tried to enforce our way of life on them. 
Why? Because we respect freedom—ours and others. That is why my first vision is that of Freedom.
I believe that India got its first vision of this in 1857, when we started the War of Independence. It is this freedom that we must protect and nurture and build on. If we are not free, no one will respect us. My second vision for India is Development. For fifty years we have been a developing nation.
It is time we saw ourselves as a developed nation. 
We are among the top five nations of the world in terms of GDP. Our poverty levels are falling.
Our achievements are being globally recognized. Yet we lack the self-confidence to see ourselves as a developed nation, self-reliant and self-assured. My third vision is that India must stand up to the world. Unless India stands up to the world, no one will respect us. Only strength respects strength.
We must be strong not only as a military power but also as an economic power."""
stemmer=PorterStemmer()

document=sent_tokenize(str)
sentence=sent_tokenize(str)
print(document)
print(type(document))


print("Apply stopword and Filter  and then Apply  portStemmer stemming ")

for i in range(len(document)):
    words=word_tokenize(document[i])
    words=[stemmer.stem(word) for word in words  if word not in set(stopwords.words('english'))]   # filter  the stop word and by then applying stemming 
    document[i]=' '.join(words)  # converting  all the  list of words into  sentences

print(document)


print("Apply stopword filter and then  apply snowball stammer ")


for i in range(len(sentence)):
    words=word_tokenize(sentence[i])
    words=[snowball.stem(word) for word in  words if word not in set(stopwords.words('english'))]
    sentence[i]=' '.join(words)

print()
print()
print(sentence)



# lEMMATIZER  

for  i in range(len(sentence)):
    words=word_tokenize(sentence[i])
    words=[lammatizer.lemmatize(word.lower(),pos='v') for word in words  if word not in set(stopwords.words('english'))]
    sentence[i]=' '.join(words)

print(sentence)

