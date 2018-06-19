from badthings import app
from badthings.services import slack
from flask import redirect, render_template


@app.route("/slack/install", methods=["GET"])
def pre_install():
    return redirect(slack.get_auth_link(), code=302)


@app.route("/slack/successful_install")
def sucessful_install():

  # Retrieve the auth code from the request params
  auth_code = request.args['code']

  # An empty string is a valid token for this request
  sc = SlackClient("")

  # Request the auth tokens from Slack
  auth_response = sc.api_call(
    "oauth.access",
    client_id=app.config['slack']['client_id'],
    client_secret=app.config['slack']['client_secret'],
    code=auth_code
  )
  return render_template('installed.html')

