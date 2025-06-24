from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
import nltk  


# in the pos_tag  we shoud  do the list of words 


str="""I have three visions for India. In 3000 years of our history, people from all over the world have come and invaded us, captured our lands, conquered our minds.
Yet we have not done this to any other nation. We have not conquered anyone.
We have not grabbed their land, their culture, their history, and tried to enforce our way of life on them. 
Why? Because we respect freedom—ours and others. That is why my first vision is that of Freedom.
I believe that India got its first vision of this in 1857, when we started the War of Independence. It is this freedom that we must protect and nurture and build on. If we are not free, no one will respect us. My second vision for India is Development. For fifty years we have been a developing nation.
It is time we saw ourselves as a developed nation. 
We are among the top five nations of the world in terms of GDP. Our poverty levels are falling.
Our achievements are being globally recognized. Yet we lack the self-confidence to see ourselves as a developed nation, self-reliant and self-assured. My third vision is that India must stand up to the world. Unless India stands up to the world, no one will respect us. Only strength respects strength.
We must be strong not only as a military power but also as an economic power."""

document=sent_tokenize(str)

print(document)


for i in range(len(document)):
    words=word_tokenize(document[i])
    words=[ word for word in  words  if word not in set(stopwords.words('english'))]
    pos_tag=nltk.pos_tag(words)
    print(pos_tag) 


str2="Tajmahal  is the   beatiful Monument"

words=word_tokenize(str2)
pos_tag1=nltk.pos_tag(words)
print(pos_tag1)


