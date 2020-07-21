import json
import numpy as np

from wrangle import utils

hotpot_dir = 'hotpot/'
wrangle_dir = 'wrangle/'
glove_file = wrangle_dir + 'glove.840B.300d.pkl'
tf_file = wrangle_dir + 'tf_1000_coref.pkl'
idf_file = wrangle_dir + 'idf_1000_coref.pkl'
hotpot_file = hotpot_dir + 'hotpot_small_1000_coref.json'
output_file = 'hotpot_small_1000_embeddings_tfidf_coref.json'

glove, hotpot, tf, idf, unk = utils.prepare_data(
    glove_file=glove_file, hotpot_file=hotpot_file, tf_file=tf_file, idf_file=idf_file)

if __name__ == "__main__":

    for idx, datum in enumerate(hotpot):
        datum['numbered_context'] = []
        datum['numbered_supporting_facts'] = []
        datum['numbered_context_flattened'] = []
        datum['numbered_context_rank'] = []
        question = datum['question']
        question_embedding = utils.sentence_embedding(
            idx, question, glove, tf, idf)
        sentence_count = 1
        for paragraph in datum['corefed_context']:
            [title, content] = paragraph
            numbered_content = []
            for sentence in content:
                numbered_content.append([sentence_count, sentence])
                embedding = utils.sentence_embedding(
                    idx, sentence, glove, tf, idf)
                sentence_similarity = utils.cosine_similarity(
                    embedding, question_embedding)
                datum['numbered_context_flattened'].append(
                    [sentence_count, sentence, title, sentence_similarity])
                sentence_count += 1
            datum['numbered_context'].append([title, numbered_content])
        sorted_sentences = sorted(
            datum['numbered_context_flattened'], key=lambda item: item[3], reverse=True)
        for sentence in sorted_sentences:
            datum['numbered_context_rank'].append(sentence[0])
        for sp_paragraph, sp_index in datum['supporting_facts']:
            paragraph = list(
                filter(lambda x: x[0] == sp_paragraph, datum['numbered_context']))
            # print(idx)
            # print(sp_paragraph, paragraph)
            if sp_index < len(paragraph[0][1]):
                overall_index = paragraph[0][1][sp_index][0]
                datum['numbered_supporting_facts'].append(overall_index)

    with open(hotpot_dir + output_file, 'w') as fp:
        json.dump(hotpot, fp)
