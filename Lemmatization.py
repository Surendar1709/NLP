from nltk.stem import WordNetLemmatizer

lemmatizer=WordNetLemmatizer()
print(lemmatizer.lemmatize("going"))


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

