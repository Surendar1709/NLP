import nltk
from nltk.tokenize import word_tokenize
#   Named enttity Recognition 


nltk.download('maxent_ne_chunker')  # downloading the named entity cheunker 
nltk.download('words')

text = "The Eiffel Tower in Paris, France was designed by Gustave Eiffel and completed in 1889 for the Exposition Universelle. It is one of the most visited monuments in the world, attracting millions of tourists every year."


words=word_tokenize(text)
for word in words:
    print(word)

#part of speech 

pos_tag=nltk.pos_tag(words)

print(pos_tag)

named_entity=nltk.ne_chunk(pos_tag).draw()
print(named_entity)


