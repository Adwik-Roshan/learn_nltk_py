from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from textblob import TextBlob

# Data gathering
reviews = [' This movie was fantastic! A must-watch.',
           'I didn\'t enjoy this movie at all.',
           'Amazing storyline and great acting!',
           'The plot was dull and predictable.',
           'Loved the cinematography! Highly recommended.',
           'fantastic movie, would watch again',
           'Amazing',
           'Ew ,terrible',
           'Never watching this',
           'my favorite']

# Data Labelling
labels = ['positive', 'negative', 'positive', 'negative', 'positive','positive','positive','negative','negative','positive']

# Reviews spell check
corrected_reviews = [str(TextBlob(rev).correct())for rev in reviews]
print(corrected_reviews)

# Vectorising
vectoriser = CountVectorizer()
x = vectoriser.fit_transform(corrected_reviews)

# Data Split
# x_train, x_test, y_train, y_test = train_test_split(
#     x, labels, test_size=0.2, random_state=42)

x_train, x_test, y_train, y_test = train_test_split(x, labels, test_size=0.25, random_state=42)

# Model Training
model = MultinomialNB()
model.fit(x_train, y_train)

# Model Testing
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test,y_pred)

print("Accuracy : ", accuracy)
# print("Vectoriser : ",x)

# Result Interpretation
if accuracy > 0.6:
    print ("the Vibes are good, book your tix! ")
else:
    print("The vibes are eh")
