import json
import pickle as pk
import re
import string

import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


class Ranker:
    stopwords = set(stopwords.words('english'))

    def __init__(self, glove_file, tf_file, idf_file):
        self.unk = np.array([0.22418134, -
                             0.28881392, 0.13854356, 0.00365387, -
                             0.12870757, 0.10243822, 0.061626635, 0.07318011, -
                             0.061350107, -
                             1.3477012, 0.42037755, -
                             0.063593924, -
                             0.09683349, 0.18086134, 0.23704372, 0.014126852, 0.170096, -
                             1.1491593, 0.31497982, 0.06622181, 0.024687296, 0.076693475, 0.13851812, 0.021302193, -
                             0.06640582, -
                             0.010336159, 0.13523154, -
                             0.042144544, -
                             0.11938788, 0.006948221, 0.13333307, -
                             0.18276379, 0.052385733, 0.008943111, -
                             0.23957317, 0.08500333, -
                             0.006894406, 0.0015864656, 0.063391194, 0.19177166, -
                             0.13113557, -
                             0.11295479, -
                             0.14276934, 0.03413971, -
                             0.034278486, -
                             0.051366422, 0.18891625, -
                             0.16673574, -
                             0.057783455, 0.036823478, 0.08078679, 0.022949161, 0.033298038, 0.011784158, 0.05643189, -
                             0.042776518, 0.011959623, 0.011552498, -
                             0.0007971594, 0.11300405, -
                             0.031369694, -
                             0.0061559738, -
                             0.009043574, -
                             0.415336, -
                             0.18870236, 0.13708843, 0.005911723, -
                             0.113035575, -
                             0.030096142, -
                             0.23908928, -
                             0.05354085, -
                             0.044904727, -
                             0.20228513, 0.0065645403, -
                             0.09578946, -
                             0.07391877, -
                             0.06487607, 0.111740574, -
                             0.048649278, -
                             0.16565254, -
                             0.052037314, -
                             0.078968436, 0.13684988, 0.0757494, -
                             0.006275573, 0.28693774, 0.52017444, -
                             0.0877165, -
                             0.33010918, -
                             0.1359622, 0.114895485, -
                             0.09744406, 0.06269521, 0.12118575, -
                             0.08026362, 0.35256687, -
                             0.060017522, -
                             0.04889904, -
                             0.06828978, 0.088740796, 0.003964443, -
                             0.0766291, 0.1263925, 0.07809314, -
                             0.023164088, -
                             0.5680669, -
                             0.037892066, -
                             0.1350967, -
                             0.11351585, -
                             0.111434504, -
                             0.0905027, 0.25174105, -
                             0.14841858, 0.034635577, -
                             0.07334565, 0.06320108, -
                             0.038343467, -
                             0.05413284, 0.042197507, -
                             0.090380974, -
                             0.070528865, -
                             0.009174437, 0.009069661, 0.1405178, 0.02958134, -
                             0.036431845, -
                             0.08625681, 0.042951006, 0.08230793, 0.0903314, -
                             0.12279937, -
                             0.013899368, 0.048119213, 0.08678239, -
                             0.14450377, -
                             0.04424887, 0.018319942, 0.015026873, -
                             0.100526, 0.06021201, 0.74059093, -
                             0.0016333034, -
                             0.24960588, -
                             0.023739101, 0.016396184, 0.11928964, 0.13950661, -
                             0.031624354, -
                             0.01645025, 0.14079992, -
                             0.0002824564, -
                             0.08052984, -
                             0.0021310581, -
                             0.025350995, 0.086938225, 0.14308536, 0.17146006, -
                             0.13943303, 0.048792403, 0.09274929, -
                             0.053167373, 0.031103406, 0.012354865, 0.21057427, 0.32618305, 0.18015954, -
                             0.15881181, 0.15322933, -
                             0.22558987, -
                             0.04200665, 0.0084689725, 0.038156632, 0.15188617, 0.13274793, 0.113756925, -
                             0.095273495, -
                             0.049490947, -
                             0.10265804, -
                             0.27064866, -
                             0.034567792, -
                             0.018810693, -
                             0.0010360252, 0.10340131, 0.13883452, 0.21131058, -
                             0.01981019, 0.1833468, -
                             0.10751636, -
                             0.03128868, 0.02518242, 0.23232952, 0.042052146, 0.11731903, -
                             0.15506615, 0.0063580726, -
                             0.15429358, 0.1511722, 0.12745973, 0.2576985, -
                             0.25486213, -
                             0.0709463, 0.17983761, 0.054027, -
                             0.09884228, -
                             0.24595179, -
                             0.093028545, -
                             0.028203879, 0.094398156, 0.09233813, 0.029291354, 0.13110267, 0.15682974, -
                             0.016919162, 0.23927948, -
                             0.1343307, -
                             0.22422817, 0.14634751, -
                             0.064993896, 0.4703685, -
                             0.027190214, 0.06224946, -
                             0.091360025, 0.21490277, -
                             0.19562101, -
                             0.10032754, -
                             0.09056772, -
                             0.06203493, -
                             0.18876675, -
                             0.10963594, -
                             0.27734384, 0.12616494, -
                             0.02217992, -
                             0.16058226, -
                             0.080475815, 0.026953284, 0.110732645, 0.014894041, 0.09416802, 0.14299914, -
                             0.1594008, -
                             0.066080004, -
                             0.007995227, -
                             0.11668856, -
                             0.13081996, -
                             0.09237365, 0.14741232, 0.09180138, 0.081735, 0.3211204, -
                             0.0036552632, -
                             0.047030564, -
                             0.02311798, 0.048961394, 0.08669574, -
                             0.06766279, -
                             0.50028914, -
                             0.048515294, 0.14144728, -
                             0.032994404, -
                             0.11954345, -
                             0.14929578, -
                             0.2388355, -
                             0.019883996, -
                             0.15917352, -
                             0.052084364, 0.2801028, -
                             0.0029121689, -
                             0.054581646, -
                             0.47385484, 0.17112483, -
                             0.12066923, -
                             0.042173345, 0.1395337, 0.26115036, 0.012869649, 0.009291686, -
                             0.0026459037, -
                             0.075331464, 0.017840583, -
                             0.26869613, -
                             0.21820338, -
                             0.17084768, -
                             0.1022808, -
                             0.055290595, 0.13513643, 0.12362477, -
                             0.10980586, 0.13980341, -
                             0.20233242, 0.08813751, 0.3849736, -
                             0.10653763, -
                             0.06199595, 0.028849555, 0.03230154, 0.023856193, 0.069950655, 0.19310954, -
                             0.077677034, -
                             0.144811], dtype='float32')

        with open(glove_file, 'rb') as fp:
            self.glove = pk.load(fp)

        with open(tf_file, 'rb') as fp:
            self.tf = pk.load(fp)

        with open(idf_file, 'rb') as fp:
            self.idf = pk.load(fp)

    def sentence_embedding(self, s):
        tokens = word_tokenize(s)
        tokens = [w for w in tokens if w not in Ranker.stopwords]
        return self.tokenized_embedding(tokens)

    def tokenized_embedding(self, tokens: list):
        embedding = np.zeros(300, dtype='float32')
        for w in tokens:
            tfidf = 0
            if (w not in self.idf):
                print("Term not found in idf.", w)
            else:
                tfidf = self.idf[w]
            if (tfidf < 0):
                tfidf = 0
            if w in self.glove:
                embedding += tfidf * self.glove[w]
            else:
                embedding += tfidf * self.unk
        embedding /= len(tokens)
        return embedding

    @staticmethod
    def cosine_similarity(a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)).item()

    def multihop_query_embedding(self, q: str, chosen_facts: list):
        query_tokens = word_tokenize(q)
        query_tokens = [w for w in query_tokens if w not in Ranker.stopwords]
        for fact in chosen_facts:
            fact_tokens = word_tokenize(fact)
            fact_tokens = [w for w in fact_tokens if w not in Ranker.stopwords]
            for token in fact_tokens:
                if token not in query_tokens:
                    query_tokens.append(token)
        return self.tokenized_embedding(query_tokens)

    def paragraph_embedding(self, paragraph: list):
        tokens = []
        title = paragraph[0]
        title_tokens = word_tokenize(title)
        for token in title_tokens:
            if token not in Ranker.stopwords:
                tokens.append(token)
        for sentence in paragraph[1]:
            sentence_tokens = word_tokenize(sentence)
            for token in sentence_tokens:
                if token not in Ranker.stopwords:
                    tokens.append(token)
        return self.tokenized_embedding(tokens)

    def rank_paragraphs(self, paragraphs: list, flattened_facts: list, question: str, chosen_fact_numbers: list):
        ranked_paragraphs = []
        chosen_facts = [flattened_facts[x - 1][1] for x in chosen_fact_numbers]
        query_embedding = self.multihop_query_embedding(
            question, chosen_facts)
        for paragraph in paragraphs:
            paragraph_embedding = self.paragraph_embedding(paragraph)
            similarity = self.cosine_similarity(
                paragraph_embedding, query_embedding)
            ranked_paragraphs.append([paragraph[0], similarity])
        ranked_paragraphs = sorted(
            ranked_paragraphs, key=lambda item: item[1], reverse=True)
        return ranked_paragraphs

    def rank_facts(self, flattened_facts: list, question: str, chosen_fact_numbers: list):
        ranked_facts = []
        chosen_facts = [flattened_facts[x - 1][1] for x in chosen_fact_numbers]
        query_embedding = self.multihop_query_embedding(
            question, chosen_facts)
        for fact in flattened_facts:
            fact_embedding = self.sentence_embedding(fact[1])
            similarity = self.cosine_similarity(
                fact_embedding, query_embedding)
            ranked_facts.append([fact[0], fact[1], fact[2], similarity])
        ranked_facts = sorted(
            ranked_facts, key=lambda item: item[3], reverse=True)
        # print(ranked_facts)
        return ranked_facts

    def rank_facts_number(self, flattened_facts: list, question: str, chosen_fact_numbers: list):
        ranked_facts = self.rank_facts(
            flattened_facts, question, chosen_fact_numbers)
        ranked_number = [x[0] for x in ranked_facts]
        return ranked_number
