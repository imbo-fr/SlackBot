# SlackBot

A simple Python SlackBot to execute custom command and action.

> Originaly based on the [digitalocean- How To Build a Slackbot in Python on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-build-a-slackbot-in-python-on-ubuntu-20-04)

# Usage

Set `SLACK_TOKEN` and `SLACK_EVENTS_TOKEN` in the **config** file.

```shell
cat <<EOF >>./config
export SLACK_TOKEN="YOUR_SLACK_TOKEN"
export SLACK_EVENTS_TOKEN="YOUR_SLACK_EVENTS_TOKEN"
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