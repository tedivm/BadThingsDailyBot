import click
from flask import Flask, session, redirect, url_for, request
from badthings import app
from badthings.services import tweets

import badthings.cli.tweets

import badthings.routes.auth
import badthings.routes.slash

@app.route('/')
def index():
    return redirect(tweets.get_random_tweet(), code=307)
