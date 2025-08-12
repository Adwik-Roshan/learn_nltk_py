import nltk
# nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize

import numpy as np

smaple_text= "I love programming "
tokens= word_tokenize(smaple_text)

print("Tokens : ", tokens)