from badthings import app
import random
import twitter


TWITTER_HANDLE='badthingsdaily'

api = twitter.Api(consumer_key=app.config['twitter']['consumer_key'],
  consumer_secret=app.config['twitter']['consumer_secret'],
  access_token_key=app.config['twitter']['access_token_key'],
  access_token_secret=app.config['twitter']['access_token_secret'])


def get_random_tweet():
    badtweets = get_all_tweets()
    random_status = random.choice(badtweets)
    return 'https://twitter.com/badthingsdaily/status/%s' % (random_status['id'])


def get_all_tweets():
    tweets = []
    max_id = None
    while True:
        batch = get_next_batch(max_id=max_id)
        if len(batch) <= 0:
            return tweets
        max_id = batch[len(batch)-1]['id']
        tweets = tweets + batch


def get_next_batch(max_id=None):
    batch = api.GetUserTimeline(screen_name=TWITTER_HANDLE,
      count=200,
      max_id=max_id,
      trim_user=True,
      exclude_replies=True)
    filtered_batch = []
    for status_tweet in batch:
        status = status_tweet.AsDict()
        if status['id'] == max_id:
            continue
        filtered_batch.append(status)
    return filtered_batch
