from badthings import app
from flask import request, url_for
from slackclient import SlackClient

sc = SlackClient(app.config['slack']['token'])
SCOPE='chat:write:bot,commands'
AUTH_BUTTON='<a href="%s"><img alt="Add to Slack" height="40" width="139" src="https://platform.slack-edge.com/img/add_to_slack.png" srcset="https://platform.slack-edge.com/img/add_to_slack.png 1x, https://platform.slack-edge.com/img/add_to_slack@2x.png 2x" /></a>'

def send_message(message, channel):
    sc.api_call(
      "chat.postMessage",
      channel=channel,
      text=message
    )

def get_redirect_url():
    return "%s%s" % (app.config['general']['url'], url_for('sucessful_install'))

def get_auth_link():
    redirect_url = get_redirect_url()
    consumer_key = app.config['slack']['client_id']
    return 'https://slack.com/oauth/authorize?scope={0}&client_id={1}&redirect_uri={2}'.format(SCOPE, consumer_key, redirect_url)


def get_auth_button():
    return AUTH_BUTTON % (get_auth_link())