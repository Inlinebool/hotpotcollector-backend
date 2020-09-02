import json
import argparse
from wrangle.file_constants import DATA_DIR, HOTPOT_RAW_FILE_NAME, HOTPOT_RAW_FILE, HOTPOT_SMALL_SIZE, HOTPOT_FILE

parser = argparse.ArgumentParser(
    description='find the index of a question in the raw data by its _id.')
parser.add_argument('target', type=str, help='Target _id.')

args = parser.parse_args()

target = args.target

with open(HOTPOT_RAW_FILE) as fp:
    big_data = json.load(fp)

pos = -1

for index, datum in enumerate(big_data):
    if datum['_id'] == target:
        pos = index

print(pos)
