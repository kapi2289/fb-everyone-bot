# -*- coding: utf-8 -*-

from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

ALL_GROUPS = os.getenv('ALL_GROUPS') == 'true'
AUTO_ACCEPT = os.getenv('AUTO_ACCEPT') == 'true'
GROUP_IDS = os.getenv('GROUP_IDS').replace(' ', '').split(',')
