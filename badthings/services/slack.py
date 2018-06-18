from badthings import app
from flask import request, url_for
from slackclient import SlackClient

sc = SlackClient(app.config['slack']['token'])
SCOPE='chat:write:bot'

def send_message(message, channel):
    sc.api_call(
      "chat.postMessage",
      channel=channel,
      text=message
    )


def get_auth_link():
    redirect_url = "%s%s" % (app.config['general']['url'], url_for('sucessful_install'))
    consumer_key = app.config['slack']['client_id']
    return 'https://slack.com/oauth/authorize?scope={0}&client_id={1}&redirect_uri={2}'.format(SCOPE, consumer_key, redirect_url)
