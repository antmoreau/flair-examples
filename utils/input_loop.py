from flair.data import Sentence


def input_loop(predict, *args):
    stop = False
    while not stop:
        try:
            sentence = input('enter a sentence :')
            if sentence == '' or sentence is None:
                print("loop stopped by user")
                stop = True
                continue
            flair_sentence = Sentence(sentence)
            predict(flair_sentence, *args)
        except KeyboardInterrupt:
            print("\n")
            print("loop stopped by user")
            stop = True
