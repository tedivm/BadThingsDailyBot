from flask import Flask
import os
import yaml
app = Flask(__name__)


if 'SETTINGS' in os.environ:
    if os.path.isfile(os.environ['SETTINGS']):
        with open(os.environ['SETTINGS'], 'r') as stream:
            app.config.update(yaml.load(stream))
    else:
        print('Unable to open settings file %s' % (os.environ['SETTINGS']))

import badthings.badthings
