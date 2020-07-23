import json
import argparse
from random import randrange
from wrangle.file_constants import DATA_DIR, HOTPOT_RAW_FILE

parser = argparse.ArgumentParser(
    description='make a smaller dataset.')
parser.add_argument('target_size', type=int, help='Target dataset size.')

args = parser.parse_args()

small_file = "hotpot_small_" + str(args.target_size) + ".json"

with open(HOTPOT_RAW_FILE) as fp:
    big_data = json.load(fp)

small_size = args.target_size

small_data_indices = set([])

for i in range(small_size):
    x = randrange(len(big_data))
    while x in small_data_indices:
        x = randrange(len(big_data))
    if x not in small_data_indices:
        small_data_indices.add(x)

small_data = [big_data[x] for x in small_data_indices]

with open(DATA_DIR + small_file, 'w') as fp:
    json.dump(small_data, fp)
