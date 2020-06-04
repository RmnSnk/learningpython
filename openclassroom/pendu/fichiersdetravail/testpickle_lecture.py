# coding: utf-8

import pickle

f = open('score.pickle', 'rb')
score = pickle.load(f)
print(score)


