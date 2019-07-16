# Messenger `@everyone` BOT

## Installation

```console
$ git clone https://github.com/kapi2289/fb-everyone-bot.git
$ cd fb-everyone-bot
$ pip install --user pipenv
$ pipenv install
```

## Configuration

You need to copy and edit .env file

```console
$ cp .env.example .env
$ nano .env
```

```bash
FB_EMAIL=email@example.com # Facebook email
FB_PASSWORD=secret # Facebook password
FB_USE_SESSION=false # Whether to use saved Facebook session (session.json file)
FB_SESSION_FILE= # Path to the session file if using

ALL_GROUPS=true # Whether to work on all groups
AUTO_ACCEPT=true # Accept all groups that someone will add you to
GROUP_IDS=99999999999,99999999999,99999999999 # Can be empty when ALL_GROUPS is true

MENTION=@everyone # Trigger text
EXACT=false # Whether if message needs to be exactly MENTION
```

## Run

```console
$ pipenv run python start.py
```
