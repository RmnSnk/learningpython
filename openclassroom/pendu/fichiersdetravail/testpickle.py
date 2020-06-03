# coding: utf-8

import pickle

score = {'romain': 3, 'sarah': 5, 'mailys': 1, 'enora': 8, 'louise': 3}

pickle.dump(score, open('score.pickle', 'wb'))


