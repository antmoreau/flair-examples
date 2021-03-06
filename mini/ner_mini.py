from flair.data import Sentence
from flair.models import SequenceTagger


# make a sentence
sentence = Sentence('Donald Duck loves Berlin .')

# load the NER tagger
tagger = SequenceTagger.load('ner')

# run NER over sentence
tagger.predict(sentence)

print(sentence.to_tagged_string())
