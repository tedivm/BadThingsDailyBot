import click
from flask import Flask, session, redirect, url_for, request, render_template
from badthings import app
from badthings.services import slack
from badthings.services import tweets

import badthings.cli.tweets

import badthings.routes.auth
import badthings.routes.slash

@app.route('/')
def index():
    button = slack.get_auth_button()
    return render_template('index.html', button=button)

@app.route('/random')
def random():
    return redirect(tweets.get_random_tweet(), code=307)
