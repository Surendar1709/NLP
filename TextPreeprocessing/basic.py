import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
print("--- Tokenization ---")
text = "NLP is fascinating. It helps computers understand human language. Let's learn more!"

# Word Tokenization
words = word_tokenize(text)
print(f"Original Text: {text}")
print(f"Word Tokens: {words}")
# Sentence Tokenization
sentences = sent_tokenize(text)
print(f"Sentence Tokens: {sentences}")
# Output: Sentence Tokens: ['NLP is fascinating.', 'It helps computers understand human language.', "Let's learn more!"]


print("\n--- Stop Words Removal ---")
text = "The quick brown fox jumps over the lazy dog and runs quickly."
stop_words = set(stopwords.words('english')) # Get English stop words

word_tokens = word_tokenize(text)
filtered_words = [word for word in word_tokens if word.lower() not in stop_words]

print(f"Original Words: {word_tokens}")
print(f"Filtered Words (no stop words): {filtered_words}")


print("\n--- Stemming vs. Lemmatization ---")
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

words_to_normalize = ["running", "runs", "ran", "program", "programming", "programs", "better", "geese"]

print("Original | Stemmed  | Lemmatized")
print("-------- | -------- | ----------")
for word in words_to_normalize:
    stemmed_word = stemmer.stem(word)
    # For lemmatization, providing the Part-of-Speech (POS) tag can improve accuracy
    # 'v' for verb is used here, but it can be 'n' for noun, 'a' for adjective etc.
    lemmatized_word = lemmatizer.lemmatize(word, pos='v') # Try as a verb first
    if stemmed_word == word and lemmatized_word == word: # If it's still the same, try as a noun
        lemmatized_word = lemmatizer.lemmatize(word, pos='n')

    print(f"{word:<8} | {stemmed_word:<8} | {lemmatized_word:<10}")


print("\n--- Part-of-Speech (POS) Tagging ---")
text = "The cat sat on the mat."
tokens = word_tokenize(text)

pos_tags = nltk.pos_tag(tokens)
print(f"Original Text: {text}")
print(f"POS Tags: {pos_tags}")


from nltk.tag import pos_tag
from nltk.chunk import ne_chunk # For NLTK's basic NER

print("\n--- Named Entity Recognition (NER) ---")
text = "Apple Inc. is headquartered in Cupertino, California. Tim Cook is the CEO."
tokens = word_tokenize(text)
pos_tags = pos_tag(tokens)

# NLTK's built-in chunker for named entities
# It builds a tree structure where named entities are grouped
named_entities_tree = ne_chunk(pos_tags)

print(f"Original Text: {text}")
print("Extracted Named Entities:")

# Function to extract entities from the tree
def extract_entities(tree):
    entities = []
    for subtree in tree:
        if isinstance(subtree, nltk.tree.Tree):
            entity_type = subtree.label()
            entity_name = " ".join([word for word, tag in subtree.leaves()])
            entities.append((entity_name, entity_type))
    return entities

extracted_entities = extract_entities(named_entities_tree)
for entity, entity_type in extracted_entities:
    print(f"- {entity_type}: {entity}")
