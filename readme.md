This repo contains the server backend for hotpot collector interfaces and scripts to wrangle data.

# Dependencies

## Python environment

For your convinience, simply create a conda environment with provided ```environment.yml```.

```conda env create -f environment.yml```

You can also manually install the following dependencies:

- python 3.8
- flask 1.1.2
- flask-cors 3.0.8
- nltk 3.5
- numpy 1.19.1

You also need to download the `stopwords` corpus for `nltk`.

```
import nltk
nltk.download('stopwords')
```

## HotpotQA Training Data

Run `bash download.sh` to download the HotpotQA training data. The script will create a folder named `data` and put the training data into the folder.

## Glove

Download the pre-trained glove embeddings from `https://www.kaggle.com/authman/pickled-glove840b300d-for-10sec-loading`, you'll need an account for kaggle (should be free to register).

Extract and put the `glove.840B.300d.pkl` file into `data` folder.

# Prepare Data

Activate `hotpot` conda environment, and then run the following commands from the project root directory:

```
python -m wrangle.make_small
python -m wrangle.coref
python -m wrangle.flatten
python -m wrangle.tf
python -m wrangle.idf
```

The first sciprt `make_small` will make a smaller dataset for local debugging. You can adjust the size of the smaller dataset by setting the `HOTPOT_SMALL_SIZE` value in `wrangle/file_constants.py`. Set the value to be empty to use the full dataset.

# Ranking and Closest Fact Experiment

To reproduce the histograms, first run `python -m wrangle.closest.py` from project root folder. It should create three json files inside `plots/closest_fact` folder. Then go to that folder and run `bash make_js.sh`. This will create three js files for easy plotting. Make sure that the file names in `make_js.sh` are consistent with the json files.

Then, open `index.html` from a modern browser, you should see the histograms.