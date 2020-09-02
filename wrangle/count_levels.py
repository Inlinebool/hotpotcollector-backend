import json
from wrangle.file_constants import HOTPOT_FILE

with open(HOTPOT_FILE) as fp:
    hotpot = json.load(fp)

easy = 0
medium = 0
hard = 0

for datum in hotpot:
    if datum['level'] == 'easy':
        easy = easy + 1
    if datum['level'] == 'medium':
        medium = medium + 1
    if datum['level'] == 'hard':
        hard = hard + 1

print(f'easy: {easy}, {easy / len(hotpot)}, medium: {medium}, {medium / len(hotpot)}, hard: {hard}, {hard / len(hotpot)}')
