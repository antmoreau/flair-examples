from flair.models import SequenceTagger
from formation.utils.input_loop import input_loop
from formation.utils.model_selection import model_selection


def predict(sentence, model):
    model.predict(sentence)
    print(sentence.to_tagged_string())


if __name__ == '__main__':
    selected_model = model_selection(default_model='ner')
    tagger = SequenceTagger.load(selected_model)
    input_loop(predict, tagger)
