# Here's how spell check generally works:

# Dictionary Comparison: The spell checker compares each word against a
# dictionary of correctly spelled words. If a word isn't found, 
# it's flagged as a potential mistake.
# Suggesting Corrections: It suggests possible corrections based on 
# common misspellings or similar words.

from textblob import TextBlob

#text w/ spelling error/s
text = " I love programing and machine learnig"

#Textblob Object
blob = TextBlob(text)

#Check Spelling 
correct_text = blob.correct()

print("Original Text : ",text)
print("Corrected Text : ",correct_text)

