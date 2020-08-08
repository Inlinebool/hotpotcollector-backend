import json
from wrangle.ranker import Ranker
from wrangle.file_constants import HOTPOT_COREF_FLATTENED_FILE, GLOVE_FILE, TF_FILE, IDF_FILE, CLOSEST_FACT_MULTIHOP_FILE, CLOSEST_FACT_ONETIME_FILE, CLOSEST_FACT_ORIGINAL_FILE

with open(HOTPOT_COREF_FLATTENED_FILE) as fp:
    data = json.load(fp)

top_sp_onetime_ranks = []
top_sp_multihop_ranks = []
top_original_pos = []
second_sp_onetime_ranks = []
second_sp_multihop_ranks = []
second_original_pos = []
third_sp_onetime_ranks = []
third_sp_multihop_ranks = []
third_original_pos = []
ranker = Ranker(GLOVE_FILE, TF_FILE, IDF_FILE)
for datum in data:
    sp_one_time_ranks = []
    original_pos = []
    ranked_facts = ranker.rank_facts(
        datum['numbered_context_flattened'], datum['question'], [])
    for fact in datum['numbered_context_flattened']:
        if fact[0] in datum['numbered_supporting_facts']:
            original_pos.append(fact[0] - 1)
    for idx, fact in enumerate(ranked_facts):
        if fact[0] in datum['numbered_supporting_facts']:
            sp_one_time_ranks.append(idx)
    sorted_sp_onetime_ranks = sorted(sp_one_time_ranks)
    sorted_original_pos = sorted(original_pos)
    if len(sorted_sp_onetime_ranks) > 0:
        top_sp_onetime_ranks.append(sorted_sp_onetime_ranks[0])
        top_sp_multihop_ranks.append(sorted_sp_onetime_ranks[0])
        top_original_pos.append(sorted_original_pos[0])
    if len(sorted_sp_onetime_ranks) > 1:
        second_sp_onetime_ranks.append(sorted_sp_onetime_ranks[1])
        second_original_pos.append(sorted_original_pos[1])

        first_fact = ranked_facts[sorted_sp_onetime_ranks[0]]
        selected_fact_positions = [first_fact[0]]
        chosen_facts = [first_fact[0]]
        ranked_facts_second = ranker.rank_facts(
            datum['numbered_context_flattened'], datum['question'], chosen_facts)
        sp_second = []
        for idx, fact in enumerate(ranked_facts_second):
            if fact[0] in datum['numbered_supporting_facts'] and fact[0] not in selected_fact_positions:
                sp_second.append(idx)
        second_sp_multihop_ranks.append(sp_second[0])
        if len(sorted_sp_onetime_ranks) > 2:
            third_sp_onetime_ranks.append(sorted_sp_onetime_ranks[2])
            third_original_pos.append(sorted_original_pos[2])

            second_fact = ranked_facts_second[sp_second[0]]
            selected_fact_positions.append(second_fact[0])
            chosen_facts.append(second_fact[0])
            ranked_facts_third = ranker.rank_facts(
                datum['numbered_context_flattened'], datum['question'], chosen_facts)
            sp_third = []
            for idx, fact in enumerate(ranked_facts_third):
                if fact[0] in datum['numbered_supporting_facts'] and fact[0] not in selected_fact_positions:
                    sp_third.append(idx)
            third_sp_multihop_ranks.append(sp_third[0])

with open(CLOSEST_FACT_ONETIME_FILE, 'w') as fp:
    json.dump({"top_sp_ranks": top_sp_onetime_ranks,
               "second_sp_ranks": second_sp_onetime_ranks,
               "third_sp_ranks": third_sp_onetime_ranks}, fp)

with open(CLOSEST_FACT_MULTIHOP_FILE, 'w') as fp:
    json.dump({"top_sp_ranks": top_sp_multihop_ranks,
               "second_sp_ranks": second_sp_multihop_ranks,
               "third_sp_ranks": third_sp_multihop_ranks}, fp)

with open(CLOSEST_FACT_ORIGINAL_FILE, 'w') as fp:
    json.dump({"top_original_pos": top_original_pos,
               "second_original_pos": second_original_pos,
               "third_original_pos": third_original_pos}, fp)
