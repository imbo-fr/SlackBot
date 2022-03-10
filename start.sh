#!/bin/bash
set -x

CUR_DIR=/volume1/homes/admin/slackbot/
cd $CUR_DIR

source ./config
source .venv/bin/activate

# IPv6
gunicorn --bind [::]:3500 main:app

# IPv4
#gunicorn --bind 0.0.0.0:3500 main:app
