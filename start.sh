#!/bin/bash

source ./config

# IPv6
/volume1/homes/admin/slackbot/.venv/bin/python -m gunicorn --bind [::]:3500 main:app

# IPv4
#/volume1/homes/admin/slackbot/.venv/bin/python -m gunicorn --bind 0.0.0.0:3500 main:app