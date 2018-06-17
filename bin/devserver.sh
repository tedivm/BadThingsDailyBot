#!/usr/bin/env bash

# Get real directory in case of symlink
if [[ -L "${BASH_SOURCE[0]}" ]]
then
  DIR="$( cd "$( dirname $( readlink "${BASH_SOURCE[0]}" ) )" && pwd )"
else
  DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
fi
DIR="$DIR/.."


source $DIR/env/bin/activate
export SETTINGS=$DIR/.settings.yaml
export FLASK_APP=$DIR/badthings/badthings.py
export DEBUG=1

flask run --host 0.0.0.0

