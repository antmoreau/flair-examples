from flair.data import Sentence
from flair.models import TextClassifier

# make a sentence
sentence = Sentence('Donald Duck loves Berlin .')
print(sentence)

# load the sentiment classifier
classifier = TextClassifier.load('en-sentiment')

# predict sentiments
classifier.predict(sentence)

# print sentence with predicted labels
print(sentence.labels)
