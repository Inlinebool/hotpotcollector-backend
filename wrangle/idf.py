import pickle as pk
import numpy as np
import json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import math
from wrangle.file_constants import HOTPOT_SMALL_COREF_FILE, IDF_FILE

stopwords = set(stopwords.words('english'))

with open(HOTPOT_SMALL_COREF_FILE, 'r') as fp:
    hotpot = json.load(fp)

idf = {}
N = 0


def extract_terms(sentence: str):
    terms = set([])
    tokens = word_tokenize(sentence)
    tokens = [w for w in tokens if w not in stopwords]
    for w in tokens:
        terms.add(w)
    update_idf(terms)


def update_idf(terms: set):
    global idf, N
    N = N + 1
    for term in terms:
        if term not in idf:
            idf[term] = 1
        else:
            idf[term] += 1


def finalize_idf():
    global idf, N
    for term in idf:
        idf[term] = math.log(N / (1 + idf[term]))


for datum in hotpot:
    terms = set([])
    extract_terms(datum['question'])
    for title, context in datum['corefed_context']:
        extract_terms(title)
        for sentence in context:
            extract_terms(sentence)

finalize_idf()
# print(idf)

with open(IDF_FILE, 'wb') as fp:
    pk.dump(idf, fp, protocol=pk.HIGHEST_PROTOCOL)
