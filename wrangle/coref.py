import json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

data_folder = "../hotpot/"
hotpot_file = 'hotpot_small_1000.json'
output_file = 'hotpot_small_1000_coref.json'

stopwords = set(stopwords.words('english'))

with open(data_folder + hotpot_file, 'r') as fp:
    hotpot = json.load(fp)

pronouns = ['it', 'It', 'they', 'They', 'she', 'She', 'he', 'He']

def coref_resolution(s: str, title: str):
    s = s.replace('\\', '\\\\')
    title = title.replace('\\', '\\\\')
    corefed_s = re.sub('|'.join(r'\b%s\b' % pronoun for pronoun in pronouns), title, s)
    corefed_s.replace('\\\\', '\\')
    return corefed_s

for datum in hotpot:
    corefed_context = []
    for title, context in datum['context']:
        corefed_paragraph = []
        for sentence in context:
            corefed_sentence = coref_resolution(sentence, title)
            corefed_paragraph.append(corefed_sentence)
        corefed_context.append([title, corefed_paragraph])
    datum['corefed_context'] = corefed_context


# print(tf)

with open(data_folder + output_file, 'w') as fp:
    json.dump(hotpot, fp)

