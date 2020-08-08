import json
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from wrangle.file_constants import HOTPOT_FILE, HOTPOT_COREF_FILE

stopwords = set(stopwords.words('english'))

with open(HOTPOT_FILE, 'r') as fp:
    hotpot = json.load(fp)

pronouns = ['it', 'It', 'they', 'They', 'she', 'She', 'he', 'He']


def coref_resolution(s: str, title: str):
    s = s.replace('\\', '\\\\')
    title = title.replace('\\', '\\\\')
    corefed_s = re.sub('|'.join(r'\b%s\b' %
                                pronoun for pronoun in pronouns), title, s)
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

with open(HOTPOT_COREF_FILE, 'w') as fp:
    json.dump(hotpot, fp)
