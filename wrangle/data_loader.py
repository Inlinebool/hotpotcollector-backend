import json
import random

from wrangle.file_constants import HOTPOT_SMALL_COREF_FLATTENED_FILE, TF_FILE, IDF_FILE, GLOVE_FILE
from wrangle.ranker import Ranker


class HotpotDataLoader:
    def __init__(self):
        with open(HOTPOT_SMALL_COREF_FLATTENED_FILE, 'r') as fp:
            self.hotpot = json.load(fp)
        self.size = len(self.hotpot)
        self.ranker = Ranker(GLOVE_FILE, TF_FILE, IDF_FILE)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    def get_datum(self, idx):
        return {'idx': idx, 'question': self.hotpot[idx]['question'], 'context': self.hotpot[idx]['numbered_context'], 'flattened_context': self.hotpot[idx]['numbered_context_flattened']}

    def get_random_datum(self, range: list, levels: dict, exclude_list: list):
        idx = random.randint(range[0], range[1])
        while not levels[self.hotpot[idx]['level']] or idx in exclude_list:
            idx = random.randint(range[0], range[1])
        return self.get_datum(idx)

    def get_ranked_facts(self, idx, chosen_facts):
        facts = self.hotpot[idx]['numbered_context_flattened']
        question = self.hotpot[idx]['question']
        return self.ranker.rank_facts(facts, question, chosen_facts)
