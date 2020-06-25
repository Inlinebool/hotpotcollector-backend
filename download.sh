
# Download Hotpot Data
wget http://curtis.ml.cmu.edu/datasets/hotpot/hotpot_dev_distractor_v1.json
wget http://curtis.ml.cmu.edu/datasets/hotpot/hotpot_dev_fullwiki_v1.json
wget http://curtis.ml.cmu.edu/datasets/hotpot/hotpot_train_v1.1.json

mkdir hotpot

mv hotpot_dev_distractor_v1.json hotpot/
mv hotpot_dev_fullwiki_v1.json hotpot/
mv hotpot_train_v1.1.json hotpot/