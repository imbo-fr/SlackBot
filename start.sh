!/bin/bash
set -x

CUR_DIR=/volume1/homes/admin/slackbot/
cd $CUR_DIR

source ./config
source .venv/bin/activate

python main.py
