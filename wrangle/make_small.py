import json
import argparse
from random import randrange
from wrangle.file_constants import DATA_DIR, HOTPOT_RAW_FILE_NAME, HOTPOT_RAW_FILE, HOTPOT_SMALL_SIZE, HOTPOT_FILE

parser = argparse.ArgumentParser(
    description='make a smaller dataset.')
parser.add_argument('--target', type=int, help='Target dataset size.')

args = parser.parse_args()

if args.target:
    small_size = args.target
    small_file = DATA_DIR + HOTPOT_RAW_FILE_NAME + \
        '_' + str(small_size) + '.json'
else:
    small_size = int(HOTPOT_SMALL_SIZE)
    small_file = HOTPOT_FILE

with open(HOTPOT_RAW_FILE) as fp:
    big_data = json.load(fp)

small_data_indices = set([])

for i in range(small_size):
    x = randrange(len(big_data))
    while x in small_data_indices:
        x = randrange(len(big_data))
    if x not in small_data_indices:
        small_data_indices.add(x)

small_data = [big_data[x] for x in small_data_indices]

with open(small_file, 'w') as fp:
    json.dump(small_data, fp)
