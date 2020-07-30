import json
import random
import datetime
import os
from flask import Flask
from flask import request
from flask_cors import CORS

from wrangle import ranker
from wrangle.data_loader import HotpotDataLoader
from wrangle.file_constants import HOTPOT_SMALL_COREF_FLATTENED_FILE, ANNOTATION_DIR, ANSWERED_LIST_FILE


app = Flask(__name__)
CORS(app)

annotations = {}

user = 'anon'
now = datetime.datetime.now()
date_time = now.strftime("%m_%d_%Y_%H:%M:%S")

data_loader = HotpotDataLoader()

user_size = int(data_loader.size / 6)

user_range = {
    'anon': [0, data_loader.size - 1],
    'josh': [0, user_size - 1],
    'mihai': [user_size, user_size * 2 - 1],
    'matt': [user_size * 2, user_size * 3 - 1],
    'kairong': [user_size * 3, user_size * 4 - 1],
    'fan': [user_size * 4, user_size * 5 - 1],
    'zhengzhong': [user_size * 5, data_loader.size - 1]
}

answered_list = set([])


def read_answered_list():
    global answered_list
    if (os.path.exists(ANSWERED_LIST_FILE)):
        with open(ANSWERED_LIST_FILE) as fp:
            answered_list = set(json.load(fp))
    else:
        answered_list = set([])



@app.route("/question", methods=['GET'])
def request_datum():
    idx = request.args.get('idx')
    if idx:
        datum_idx = int(request.args.get('idx'))
        return data_loader.get_datum(datum_idx)
    else:
        user = request.args.get('user')
        easy = request.args.get('easy') == 'true'
        medium = request.args.get('medium') == 'true'
        hard = request.args.get('hard') == 'true'
        levels = {'easy': easy, 'medium': medium, 'hard': hard}
        range = user_range[user]
        read_answered_list()
        return data_loader.get_random_datum(range, levels, answered_list)


@app.route("/answer", methods=['POST'])
def get_answer():
    data = request.get_json()

    now = datetime.datetime.now()
    date_time = now.strftime("%m_%d_%Y_%H:%M:%S")

    annotation_filename = ANNOTATION_DIR + 'annotation_' + \
        data['user'] + '_' + date_time + ".json"
    annotations = {}
    annotations['user'] = data['user']
    annotations['time'] = date_time
    annotations['levels'] = data['levels']
    annotations['data'] = data['data']

    with open(annotation_filename, 'w') as fp:
        json.dump(annotations, fp)

    global answered_list
    if (data['data']['answer']):
        answered_list.add(int(data['data']['idx']))
        with open(ANSWERED_LIST_FILE, 'w') as fp:
            json.dump(list(answered_list), fp)

    return {"success": "true"}
