First end tp end Project


#dagshub

MLFLOW_TRACKING_URI=https://dagshub.com/neelamghavate/fsds_end2end.mlflow \
MLFLOW_TRACKING_USERNAME=neelamghavate \
MLFLOW_TRACKING_PASSWORD=94b6a0e9195d188bf5da7bee35e9d35b5efb9f9a  \
python script.py

#Run this to export as env variables:

export MLFLOW_TRACKING_URI=https://dagshub.com/neelamghavate/fsds_end2end.mlflow

export MLFLOW_TRACKING_USERNAME=neelamghavate

export MLFLOW_TRACKING_PASSWORD=94b6a0e9195d188bf5da7bee35e9d35b5efb9f9a


##DVC COMMANDS

dvc init
dvc add D:\ineuron\fsds_end2end\notebooks\data\gemstone.csv
create file dvc.yaml with code
dvc.repro