import json

processed_file = "../../hotpot/hotpot_small_1000_embeddings_tfidf_coref.json"

with open(processed_file) as fp:
    data = json.load(fp)

top_sp_ranks = []
top_original_pos = []
second_sp_ranks = []
second_original_pos = []
third_sp_ranks = []
third_original_pos = []
for datum in data:
    sp_ranks = []
    original_pos = []
    for pos in datum["numbered_supporting_facts"]:
        original_pos.append(pos - 1)
        sp_rank = -1
        for idx, rank in enumerate(datum["numbered_context_rank"]):
            if rank == pos:
                sp_rank = idx
        sp_ranks.append(sp_rank)
    sorted_sp_ranks = sorted(sp_ranks)
    sorted_original_pos = sorted(original_pos)
    if len(sorted_sp_ranks) > 0:
        top_sp_ranks.append(sorted_sp_ranks[0])
        top_original_pos.append(sorted_original_pos[0])
    if len(sorted_sp_ranks) > 1:
        second_sp_ranks.append(sorted_sp_ranks[1])
        second_original_pos.append(sorted_original_pos[1])
    if len(sorted_sp_ranks) > 2:
        third_sp_ranks.append(sorted_sp_ranks[2])
        third_original_pos.append(sorted_original_pos[2])

with open("closest_fact_1000_tfidf_coref.json", 'w') as fp:
    json.dump({"top_sp_ranks": top_sp_ranks,
               "second_sp_ranks": second_sp_ranks,
               "third_sp_ranks": third_sp_ranks}, fp)

with open("original_pos_1000.json", 'w') as fp:
    json.dump({"top_original_pos": top_original_pos,
               "second_original_pos": second_original_pos,
               "third_original_pos": third_original_pos}, fp)
