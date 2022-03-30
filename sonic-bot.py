import os
import datetime
from slack import WebClient
from slack.errors import SlackApiError

slack_token = os.environ["SLACK_API_TOKEN"]
client = WebClient(token = slack_token)

sonic_release = datetime.datetime(2022,4,8)
time_to_release = sonic_release - date.today()

try:
  response = client.chat_postMessage(
    channel="slack-bots",
    text="Hello from Sonic! There are "+time_to_release+ " days until Sonic 2 hits theaters. Gotta go fast :checkered_flag:"
  )
except SlackApiError as e:
  # You will get a SlackApiError if "ok" is False
  assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
  
  