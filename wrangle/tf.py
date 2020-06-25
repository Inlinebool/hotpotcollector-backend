import pickle as pk
import numpy as np
import json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import math

data_folder = "../hotpot/"
hotpot_file = 'hotpot_small_1000_coref.json'
output_file = 'tf_1000_coref.pkl'

stopwords = set(stopwords.words('english'))

with open(data_folder + hotpot_file, 'r') as fp:
    hotpot = json.load(fp)

def extract_terms(terms: dict, sentence: str):
    tokens = word_tokenize(sentence)
    tokens = [w for w in tokens if w not in stopwords]
    for w in tokens:
        if w not in terms:
            terms[w] = 1
        else:
            terms[w] += 1

def compute_tf(terms: dict):
    max_term = max(terms, key=lambda k: terms[k])
    max_tf = terms[max_term]
    for term in terms:
        # don't normalize
        terms[term] /= max_tf
    return terms

tf = []
N = len(hotpot)

for datum in hotpot:
    terms = {}
    extract_terms(terms, datum['question'])
    for title, context in datum['corefed_context']:
        extract_terms(terms, title)
        for sentence in context:
            extract_terms(terms, sentence)
    tf.append(terms)

# print(tf)

with open(output_file, 'wb') as fp:
    pk.dump(tf, fp, protocol=pk.HIGHEST_PROTOCOL)

