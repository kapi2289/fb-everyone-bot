# -*- coding: utf-8 -*-

import fbchat
from fbchat.models import *
from variables import *
from utils import *


class Client(fbchat.Client):

    def onMessage(self, message_object, author_id, thread_id, thread_type, **kwargs):
        if self.uid == author_id:
            return
        if thread_type != ThreadType.GROUP:
            return
        if not ALL_GROUPS and thread_id not in GROUP_IDS:
            return
        if not EXACT and MENTION not in message_object.text:
            return
        if EXACT and message_object.text != MENTION:
            return
        group = self.fetchGroupInfo(thread_id)[thread_id]
        mentions = [Mention(uid, 0, len(MENTION)) for uid in group.participants]
        self.send(Message(text=MENTION, mentions=mentions), thread_id=thread_id, thread_type=thread_type)

    @d_if(AUTO_ACCEPT)
    def onInbox(self, **kwargs):
        self.acceptPending()

    def acceptPending(self):
        thread_ids = []
        thread_ids += [thread.uid for thread in self.fetchThreadList(thread_location=ThreadLocation.PENDING, limit=20)
            if thread.type == ThreadType.GROUP]
        thread_ids += [thread.uid for thread in self.fetchThreadList(thread_location=ThreadLocation.OTHER, limit=20)
            if thread.type == ThreadType.GROUP]
        self.moveThreads(ThreadLocation.INBOX, thread_ids)


if __name__ == "__main__":
    client = Client(EMAIL, PASSWORD)
    client.listen()
