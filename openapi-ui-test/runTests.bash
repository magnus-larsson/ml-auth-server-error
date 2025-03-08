#!/usr/bin/env bash

#
#  INTERACTIVE=true DO_LOGIN=true ./runTests.bash
#
: ${DO_LOGIN=true}
: ${INTERACTIVE=false}
set -e

# Determining script location, and set the working directory to the script location
SCRIPT_DIR=$(cd $( dirname "${BASH_SOURCE[0]}") && pwd)
cd $SCRIPT_DIR


python3 -m venv env
source ./env/bin/activate
pip install --upgrade pip --quiet
pip install -r requirements.txt --quiet

args=""

if [[ $DO_LOGIN == "true" ]]
then
  args+=" login"
fi

if [[ $INTERACTIVE == "true" ]]
then
  args+=" interactive"
fi

python3 test-openapi-ui.py $args

deactivate
