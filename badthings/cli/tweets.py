from badthings import app
from badthings.services import slack
from badthings.services import tweets
import random


@app.cli.command()
def verify_credentials():
    print(tweets.api.VerifyCredentials())


@app.cli.command()
def get_tweet_count():
    badtweets = tweets.get_all_tweets()
    print(len(tweets.get_all_tweets()))


@app.cli.command()
def get_random_tweet():
    print(tweets.get_random_tweet())


@app.cli.command()
def send_tweet_to_slack():
    slack.send_message(tweets.get_random_tweet(), '@ali')
