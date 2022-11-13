import os
import re

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler


from util import *

# Logging (local_functions)
init_logger('output.log','WARN','INFO')

app = App(token=os.environ["SLACK_BOT_TOKEN"])

# Commands need to be defined in your bot at api.slack.com
# See Features - Slash Commands
@app.command("/hello-bolt")
def hello(body, ack):
    ack(f"Hi <@{body['user_id']}>!")

@app.command("/boot-fixe")
def boot_fixe(body, ack):
    cmd = '/usr/syno/sbin/synonet --wake D4:3D:7E:EA:6A:8F eth0'
    with os.popen(cmd) as res:
        print(res.readlines())
    ack(f"Command done!")

@app.command("/boot-fixe-antoine")
def boot_fixe(body, ack):
    cmd = '/usr/syno/sbin/synonet --wake D4:3D:7E:EA:6A:8F eth0'
    with os.popen(cmd) as res:
        print(res.readlines())
    ack(f"Command done!")

@app.command("/boot-fixe-magalie")
def boot_fixe(body, ack):
    cmd = '/usr/syno/sbin/synonet --wake D8:50:E6:40:E7:F7 eth0'
    with os.popen(cmd) as res:
        print(res.readlines())
    ack(f"Command done!")

@app.message(re.compile("(hello|hi)", re.I))
def say_hello_regex(say, context):
    greeting = context["matches"][0]
    say(f"{greeting}, <@{context['user_id']}>, how are you?")

@app.message(re.compile(""))
def catch_all(say, context):
    """A catch-all message."""
    say(f"I didn't get that, <@{context['user_id']}>.")


@app.event("app_mention")
def handle_app_mention_events(body, client, say):
    # Reply to mentions in a thread.
    client.chat_postMessage(
        channel=body["event"]["channel"],
        thread_ts=body["event"]["thread_ts"],
        text=f"Yes <@{body['event']['user']}>.",
    )


if __name__ == "__main__":
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()
