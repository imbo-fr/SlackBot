# SlackBot

A simple Python SlackBot to execute custom command and action on FreeBSD system with service (OpnSense)

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

Start the bot

```shell
export SLACK_APP_TOKEN="REDACTED"
export SLACK_BOT_TOKEN="REDACTED"
.venv/bin/python3 main.py
```

# Deploy as a service on FreeBSD

Create the service

```shell
cat <<EOF >>/usr/local/etc/rc.d/slackbot
#!/bin/sh

# PROVIDE: slackbot
# REQUIRE: DAEMON
# KEYWORD: shutdown

. /etc/rc.subr

name="slackbot"
rcvar="slackbot_enable"

# Env vars
export SLACK_APP_TOKEN="REDACTED"
export SLACK_BOT_TOKEN="REDACTED"

# PID file management (optional but recommended for background services)
pidfile="/var/run/${name}.pid"

# --- CONFIGURATION ---
script_dir="/usr/local/SlackBot"
python_venv="${script_dir}/.venv/bin/python3"
script_file="${script_dir}/main.py"

# Use daemon:
# -S : Syslog
# -T : Tag
# -f : Fork (background)
# -r : Restart automatically if it crashes
# -P : PID file
command="/usr/sbin/daemon"
command_args="-S -T slackbot -f -r -P ${pidfile} ${python_venv} ${script_file}"

load_rc_config $name
run_rc_command "$1"
EOF
```

Enable service auto-start 

```shell
cat <<EOF >>/etc/rc.conf.d/slackbot
slackbot_enable="YES"
EOF


Then you can manage the service

```
service slackbot start
service slackbot status
service slackbot stop

service slackbot enable
```
