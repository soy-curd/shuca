#!/usr/bin/python
# -*- coding: utf-8 -*-

class Instantiate:

    def __init__(self, dict_path):
        self.dict = {}
        self.ReadDictionary(dict_path)
        self.sentence_weights = []

    def ReadDictionary(self, dict_path):
        f = open(dict_path, 'r')
        for line in f.readlines():
            # TODO: change to utf-8
            line = str(line)
            line = line.rstrip()
            (feature, weight) = line.split('\t')
            self.dict[feature] = weight

    def CalculateSentenceWeights(self, features):
        for feature in features:
            score = 0
            for key, value in list(feature.items()):
                if key in self.dict:
                    score = score + float(value) * float(self.dict[key])
            self.sentence_weights.append(score)

    def GetSentenceWeights(self):
        return self.sentence_weights

if __name__ == '__main__':
    pass
