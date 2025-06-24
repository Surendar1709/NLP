from nltk.tokenize import sent_tokenize, word_tokenize, wordpunct_tokenize, TreebankWordTokenizer

corpos = """Reading is a fundamental skill that significantly impacts personal and academic growth. 
It enhances vocabulary, improves comprehension, and fosters critical thinking. 
When individuals read regularly, they are exposed to new ideas and perspectives,
which broadens their understanding of the world. Additionally, reading stimulates the brain, keeping it active and engaged,
which can help prevent cognitive decline.
It also provides a means of relaxation and stress reduction, 
as immersing oneself in a good book can be a soothing escape from daily pressures. 
Therefore, cultivating a habit of reading not only contributes to intellectual development but also promotes overall well-being."""

# Sentence tokenization
document = sent_tokenize(corpos)
print("Sentence Tokenization:")
for sent in document:
    print(sent)

    

# Word tokenization
print("\nWord Tokenization:")
words = word_tokenize(corpos)
for w in words:
    print(w)

# WordPunct tokenization
print("\nWordPunct Tokenization:")
word_punct = wordpunct_tokenize(corpos)
print(word_punct)

# TreebankWordTokenizer
print("\nTreebank Word Tokenization:")
treebank = TreebankWordTokenizer()
treebank_tokens = treebank.tokenize(corpos)
print(treebank_tokens)
