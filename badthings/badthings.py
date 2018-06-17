import click
from flask import Flask, session, redirect, url_for, request
from badthings import app
import badthings.cli.tweets
import badthings.routes.slash
from badthings.services import tweets


@app.route('/')
def index():
    return redirect(tweets.get_random_tweet(), code=307)
