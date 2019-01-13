# Messenger `@everyone` BOT

## Installation

```console
$ git clone https://github.com/kapi2289/fb-everyone-bot.git
$ cd fb-everyone-bot
$ python -m pip install -r requirements.txt
```

## Configuration

You need to copy and edit .env file

```console
$ cp .env.example .env
$ nano .env
```

```bash
EMAIL="email@example.com" # Facebook email
PASSWORD="secret" # Facebook password

ALL_GROUPS=true # Work on all groups
AUTO_ACCEPT=true # Accept all groups that someone will add you to
GROUP_IDS="99999999999, 99999999999, 99999999999" # Can be empty when ALL_GROUPS is true
```

## Run

```console
$ python run.py
```
