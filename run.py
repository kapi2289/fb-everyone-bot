# -*- coding: utf-8 -*-

import fbchat
from variables import *


class Client(fbchat.Client):
    pass

if __name__ == "__main__":
    client = Client(EMAIL, PASSWORD)
    client.listen()

