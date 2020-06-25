import json
from random import randrange
import argparse

parser = argparse.ArgumentParser(
    description='make a smaller dataset.')
parser.add_argument('target_size', type=int, help='Target dataset size.')

args = parser.parse_args()

data_folder = "../hotpot/"
big_file = "hotpot_train_v1.1.json"

small_file = "hotpot_small_" + str(args.target_size) + ".json"

with open(data_folder + big_file) as fp:
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

with open(data_folder + small_file, 'w') as fp:
    json.dump(small_data, fp)
