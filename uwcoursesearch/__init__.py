from flask import Flask
import os

app = Flask(__name__)

#Set up configuration
app.config.from_object(__name__)
app.config['API_KEY'] = os.environ['API_KEY']

app.config.update(dict(
    SECRET_KEY='development key',
))

import uwcoursesearch.views
