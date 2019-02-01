# -*- coding: utf-8 -*-

from dotenv import load_dotenv
import os

load_dotenv()

def is_true(a):
    return a.lower() in ("true", "yes", "1")

FB_EMAIL = os.getenv('FB_EMAIL')
FB_PASSWORD = os.getenv('FB_PASSWORD')

ALL_GROUPS = is_true(os.getenv('ALL_GROUPS'))
AUTO_ACCEPT = is_true(os.getenv('AUTO_ACCEPT'))
GROUP_IDS = os.getenv('GROUP_IDS').split(',')

MENTION = os.getenv('MENTION')
EXACT = is_true(os.getenv('EXACT'))
