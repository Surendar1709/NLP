from nltk.stem import WordNetLemmatizer

# here  we get the root word  which is called lemma 

#consume  more time  when compare to  stemmeing 
# usecase of lemmatization is  Q&A  chatbot,text, summarization 

# lamitization having the dictnary of all the root words   having the gramtical form of the word 

lemmatizer=WordNetLemmatizer()  #  creating the  object for the  wordnetlemmatizer class 
print(lemmatizer.lemmatize("going",pos='v'))

print(lemmatizer.lemmatize("going",pos='a'))
print(lemmatizer.lemmatize("folding",pos='r'))  #  lammatize (word,pos)


print("Lemmatizer the  list  of  words")
words = [
    'running', 'ran', 'runs', 'easily', 'fairly',
    'better', 'best', 'am', 'is', 'are', 'was', 'were',
    'has', 'have', 'had', 'cats', 'children', 'geese',
    'feet', 'mice', 'studies', 'leaves', 'went',
    'swimming', 'happier', 'happiest', 'flying', 'flies',
    'denied', 'dying', 'meeting', 'itemization'
]
for word in words:
    print(word+"------>"+lemmatizer.lemmatize(word,pos="v"))


print(lemmatizer.lemmatize("fairly",pos='v'))
print(lemmatizer.lemmatize("sportingly",pos='v'))


print("Lemmatizer the  list  of  words")



