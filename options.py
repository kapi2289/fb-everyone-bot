# -*- coding: utf-8 -*-

import json
import os

from dotenv import load_dotenv

load_dotenv()


def is_true(a):
    return a.lower() in ("true", "yes", "1")


FB_EMAIL = os.getenv('FB_EMAIL')
FB_PASSWORD = os.getenv('FB_PASSWORD')
FB_USE_SESSION = is_true(os.getenv('FB_USE_SESSION'))
FB_SESSION_FILE = os.getenv("FB_SESSION_FILE") or "session.json"

with open(FB_SESSION_FILE) as f:
    FB_SESSION = json.loads(f.read()) if FB_USE_SESSION else None

ALL_GROUPS = is_true(os.getenv('ALL_GROUPS'))
AUTO_ACCEPT = is_true(os.getenv('AUTO_ACCEPT'))
GROUP_IDS = os.getenv('GROUP_IDS').split(',')

MENTION = os.getenv('MENTION')
EXACT = is_true(os.getenv('EXACT'))
