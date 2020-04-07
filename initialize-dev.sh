#!/usr/bin/env bash

python3 -m venv env

source .envrc

pip3 install wheel tox
pip3 install -r requirements.txt
