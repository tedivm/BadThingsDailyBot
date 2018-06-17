from badthings import app
from slackclient import SlackClient

sc = SlackClient(app.config['slack']['token'])

def send_message(message, channel):
    sc.api_call(
      "chat.postMessage",
      channel=channel,
      text=message
    )
