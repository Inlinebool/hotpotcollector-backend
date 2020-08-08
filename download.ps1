if (! (Test-Path -Path "data")) {
    mkdir data
}

if (! (Test-Path -Path "data/hotpot_train_v1.1.json")) {
    Invoke-WebRequest http://curtis.ml.cmu.edu/datasets/hotpot/hotpot_train_v1.1.json -OutFile data/hotpot_train_v1.1.json
}
