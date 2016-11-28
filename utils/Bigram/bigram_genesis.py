import string
import random
import numpy as np


class BigramLanguageModel(object):
    freqs = None
    bigrams = None
    def __init__(self, filename=None):
        if filename is not None:
            self.buildLanguageModel(filename)
        return

    def buildLanguageModel(self, filename):
        fn = open(filename, 'r')
        words = [w.strip().lower().translate(None, string.punctuation) for w in fn.read().split()]

        freqs = {}
        bigrams = {}
        for i in xrange(len(words) - 1):
            if words[i] not in freqs:
                freqs[words[i]] = 0
            if words[i] not in bigrams:
                bigrams[words[i]] = {}
            if words[i+1] not in bigrams[words[i]]:
                bigrams[words[i]][words[i+1]] = 0

            freqs[words[i]] += 1
            bigrams[words[i]][words[i+1]] += 1

        for word in bigrams.keys():
            for next_word in bigrams[word]:
                probability = float(bigrams[word][next_word])/freqs[word]
                bigrams[word][next_word] = probability

        for word in freqs.keys():
            freqs[word] = float(freqs[word])/len(freqs)

        self.freqs = freqs
        self.bigrams = bigrams
        return

    def generate_next_word(self, word):
        w = word.strip().lower().translate(None, string.punctuation)
        # index = np.max(np.random.rand() > np.cumsum(self.bigrams[w].values())).nonzero()[0])
        nonzero_indices = (np.random.rand() > np.cumsum(self.bigrams[w].values())).nonzero()[0]
        if len(nonzero_indices):
            index = np.max(nonzero_indices)
        else:
            index = 0
        return self.bigrams[w].keys()[index]

    def generate_random_sentence(self, length=20, start="The"):
        generated = [start]
        for i in xrange(1, length):
            generated.append(self.generate_next_word(generated[i-1]))
        return " ".join(generated)

if __name__ == '__main__':
    filename = raw_input("enter file name: ")
    lm = LanguageModel(filename)
    print lm.generate_random_sentence(20)
