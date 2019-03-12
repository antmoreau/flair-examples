from flair.data import Sentence
from flair.models import SequenceTagger


# make a sentence
sentence = Sentence('Donald Duck and his car love Berlin .')

# load the POS tagger
tagger = SequenceTagger.load('pos')

# run POS over sentence
tagger.predict(sentence)

print(sentence.to_tagged_string())
