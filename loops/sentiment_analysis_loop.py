from flair.models import TextClassifier
from formation.utils.input_loop import input_loop


def predict(sentence, model):
    model.predict(sentence)
    sentiment = sentence.labels[0]
    if sentiment.score < 0.33:
        print('polarity: ' + str(sentiment.score) + ' ---> NEUTRAL')
        return
    print('polarity: ' + str(sentiment.score) + ' ---> ' + sentiment.value)


if __name__ == '__main__':
    classifier = TextClassifier.load('en-sentiment')
    input_loop(predict, classifier)
