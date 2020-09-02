DATA_DIR = 'data/'
PLOT_DIR = 'plots/'
ANNOTATION_DIR = 'user_annotations/'
HOTPOT_SMALL_SIZE = ""
GLOVE_FILE = DATA_DIR + 'glove.840B.300d.pkl'

HOTPOT_RAW_FILE_NAME = 'hotpot_train_v1.1'
HOTPOT_RAW_FILE = DATA_DIR + HOTPOT_RAW_FILE_NAME + '.json'

if HOTPOT_SMALL_SIZE:
    SMALL_SUBFIX = '_' + HOTPOT_SMALL_SIZE
else:
    SMALL_SUBFIX = ''

HOTPOT_FILE = DATA_DIR + HOTPOT_RAW_FILE_NAME + SMALL_SUBFIX + '.json'
HOTPOT_COREF_FILE = DATA_DIR + HOTPOT_RAW_FILE_NAME + SMALL_SUBFIX + '_coref.json'
HOTPOT_COREF_FLATTENED_FILE = DATA_DIR + HOTPOT_RAW_FILE_NAME + \
    SMALL_SUBFIX + '_coref_flattened.json'

TF_FILE = DATA_DIR + 'tf' + SMALL_SUBFIX + '_coref.pkl'
IDF_FILE = DATA_DIR + 'idf' + SMALL_SUBFIX + '_coref.pkl'
CLOSEST_FACT_DIR = PLOT_DIR + 'closest_fact/'
CLOSEST_FACT_ONETIME_FILE = CLOSEST_FACT_DIR + \
    'closest_fact' + SMALL_SUBFIX + '_onetime.json'
CLOSEST_FACT_MULTIHOP_FILE = CLOSEST_FACT_DIR + \
    'closest_fact' + SMALL_SUBFIX + '_multihop.json'
CLOSEST_FACT_ORIGINAL_FILE = CLOSEST_FACT_DIR + \
    'closest_fact' + SMALL_SUBFIX + '_original.json'

ANSWERED_LIST_FILE = 'answered_questions.json'

FIXED_PRACTICE_QUESTIONS = [21041, 0]
FIXED_BASIC_QUESTIONS = [2, 3, 4]
FIXED_RANKED_QUESTIONS = [5, 6, 7]

EASY_SIZE = 1
MEDIUM_SIZE = 5
HARD_SIZE = 1