import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

sample_text = "I am learning n-grams within NLP(Natural Language Processing)"
tokens = word_tokenize(sample_text)

print("Tokens : ", tokens)

#unigram
unigrams = list(ngrams(tokens,1))
print("Unigrams : ",unigrams)

#Bigrams
bigrams = list(ngrams(tokens,2))
print("Bigrams : ",bigrams)

#Trigrams
trigrams = list(ngrams(tokens,3))
print("Trigrams : ", trigrams)