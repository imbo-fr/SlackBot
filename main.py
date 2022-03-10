import os
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter
from slackbot import SlackBot

from util import *

# Logging (local_functions)
init_logger('output.log','WARN','INFO')

# Initialize a Flask app to host the events adapter
app = Flask(__name__)
# Create an events adapter and register it to an endpoint in the slack app for event injestion.
slack_events_adapter = SlackEventAdapter(os.environ.get("SLACK_EVENTS_TOKEN"), "/slack/events", app)

# Initialize a Web API client
slack_web_client = WebClient(token=os.environ.get("SLACK_TOKEN"))

def flip_coin(channel):
    """Craft the SlackBot, flip the coin and send the message to the channel
    """
    # Create a new SlackBot
    slack_bot = SlackBot(channel)

    # Get the onboarding message payload
    message = slack_bot.get_message_payload()

    # Post the onboarding message in Slack
    slack_web_client.chat_postMessage(**message)


# When a 'message' event is detected by the events adapter, forward that payload
# to this function.
@slack_events_adapter.on("message")
def message(payload):
    """Parse the message event, and if the activation string is in the text,
    simulate a coin flip and send the result.
    """

    # Get the event data from the payload
    event = payload.get("event", {})

    # Get the text from the event that came through
    text = event.get("text")

    # Check and see if the activation phrase was in the text of the message.
    # If so, execute the code to flip a coin.
    if "hey sammy, flip a coin" in text.lower():
        return flip_coin(event.get("channel"))

if __name__ == "__main__":
    # Run our app
    app.run()
