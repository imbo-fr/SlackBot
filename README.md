# SlackBot

A simple Python SlackBot to execute custom command and action on Synology system (non-docker).

> Originaly based on the [How to write a modern Slack bot in Python](https://www.stavros.io/posts/how-to-slack-bot/)

# Requirement

- Python 3
- Python packages `virtualenv` or `venv`

# Install

Create and use a Python virtual environnement to install packages

```shell
python3 -m virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

# Usage

In the cloned folder, create **config** file with slack credentials.

```shell
cat <<EOF >>./config
export SLACK_APP_TOKEN="YOUR_SLACK_APP_TOKEN"
export SLACK_BOT_TOKEN="YOUR_SLACK_BOT_TOKEN"
EOF
```

Start the bot

```shell
./start.sh
```

# Deploy as a service on Synology

Create the synology service file

```shell
cat <<EOF >>/etc/init/slackbot.conf
# only start this service after the sshd process has started
start on started sshd

# stop the service gracefully if the runlevel changes to 'reboot'
stop on runlevel [06]

# exec the process.
exec /volume1/homes/admin/slackbot/start.sh
EOF
```

Then you can manage the service

```
start slackbot
status slackbot
stop slackbot
```