import click
from flask import Flask, jsonify, request
from badthings import app
from badthings.services import tweets

@app.route('/slash/single', methods = ['GET', 'POST'])
def slash_single():
    scenario = tweets.get_random_tweet()
    response = {
        'response_type': 'in_channel',
        'text': scenario
    }
    return jsonify(response)
