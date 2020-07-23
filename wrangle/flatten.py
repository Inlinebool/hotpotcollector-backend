import json
import numpy as np

from wrangle.file_constants import HOTPOT_SMALL_COREF_FILE, HOTPOT_SMALL_COREF_FLATTENED_FILE

with open(HOTPOT_SMALL_COREF_FILE, 'r') as fp:
    hotpot = json.load(fp)

for idx, datum in enumerate(hotpot):
    datum['numbered_context'] = []
    datum['numbered_supporting_facts'] = []
    datum['numbered_context_flattened'] = []
    sentence_count = 1
    for paragraph in datum['corefed_context']:
        [title, content] = paragraph
        numbered_content = []
        for sentence in content:
            numbered_content.append([sentence_count, sentence])
            datum['numbered_context_flattened'].append(
                [sentence_count, sentence, title])
            sentence_count += 1
        datum['numbered_context'].append([title, numbered_content])
    for sp_paragraph, sp_index in datum['supporting_facts']:
        paragraph = list(
            filter(lambda x: x[0] == sp_paragraph, datum['numbered_context']))
        if sp_index < len(paragraph[0][1]):
            overall_index = paragraph[0][1][sp_index][0]
            datum['numbered_supporting_facts'].append(overall_index)

with open(HOTPOT_SMALL_COREF_FLATTENED_FILE, 'w') as fp:
    json.dump(hotpot, fp)
