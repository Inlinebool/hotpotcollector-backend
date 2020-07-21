from flask import Flask
from flask import render_template
from flask import request
from flask_cors import CORS
import json
import random
import datetime
import os


def new_annotation(user, date_time, levels):
    global annotations
    global annotation_filename
    annotation_filename = 'user_annotations/annotation_' + \
        user + '_' + date_time + ".json"
    annotations = {}
    annotations['user'] = user
    annotations['time'] = date_time
    annotations['levels'] = levels
    annotations['data'] = []


app = Flask(__name__)
CORS(app)

dataset_filename = "hotpot/hotpot_small_1000_embeddings_tfidf_coref.json"

annotation_filename = "user_annotations/anotation.json"

answered_list_filename = "answered_questions.json"

annotations = {}

user = 'anon'
now = datetime.datetime.now()
date_time = now.strftime("%m_%d_%Y_%H:%M:%S")
new_annotation(user, date_time, {'easy': True, 'medium': True, 'hard': True})

user_range = {
    'anon': [0, 1000],
    'josh': [0, 15074],
    'mihai': [15075, 30148],
    'matt': [30149, 45222],
    'kairong': [45223, 60296],
    'fan': [60297, 75370],
    'zhengzhong': [75371, 90447]
}

levels = {'easy': True, 'medium': True, 'hard': True, }

with open(dataset_filename) as fp:
    dataset = json.load(fp)

if (os.path.exists(answered_list_filename)):
    with open(answered_list_filename) as fp:
        answered_list = set(json.load(fp))
        print(answered_list)
else:
    answered_list = set([])


# @app.route("/", methods=['GET'])
# def index():
#     return render_template('index.html')


# @app.route("/collector", methods=['GET'])
# def collector():
#     return render_template('collector.html')


@app.route("/question", methods=['GET'])
def request_datum():
    idx = request.args.get('idx')
    if idx:
        datum_idx = int(request.args.get('idx'))
        print(datum_idx)
    else:
        range = user_range[user]
        datum_idx = random.randint(range[0], range[1])
        print(dataset[datum_idx]['level'])
        while not levels[dataset[datum_idx]['level']] or datum_idx in answered_list:
            datum_idx = random.randint(range[0], range[1])
            print(dataset[datum_idx]['level'])

    return {'idx': datum_idx, 'data': dataset[datum_idx]}


@app.route("/setuser", methods=['POST'])
def setuser():
    data = request.get_json()
    print(data)
    global user
    user = data['user']
    global levels
    levels = data['levels']
    global annotation_filename
    global annotations
    now = datetime.datetime.now()
    date_time = now.strftime("%m_%d_%Y_%H:%M:%S")
    new_annotation(user, date_time, levels)
    return {"success": "true"}


@app.route("/answer", methods=['POST'])
def get_answer():
    print("handling post")
    # print(request.values)
    print(request.get_json())
    data = request.get_json()

    annotations['data'].append(data)
    answered_list.add(data['idx'])

    print(annotations)

    with open(annotation_filename, 'w') as fp:
        json.dump(annotations, fp)

    return {"success": "true"}
