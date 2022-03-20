# SlackBot

A simple Python SlackBot to execute custom command and action on Synology system (non-docker).

> Originaly based on the [How to write a modern Slack bot in Python](https://www.stavros.io/posts/how-to-slack-bot/)

# Usage

Set `SLACK_TOKEN` and `SLACK_BOT_TOKEN` in the **config** file.

```shell
cat <<EOF >>./config
export SLACK_APP_TOKEN="YOUR_SLACK_APP_TOKEN"
export SLACK_BOT_TOKEN="YOUR_SLACK_BOT_TOKEN"

EOF
```

```shell
pip install -r requirements.txt
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