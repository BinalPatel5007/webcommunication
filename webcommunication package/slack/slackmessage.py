#!/usr/bin/env python
# coding: utf-8

# In[108]:


import slack
import calendar
from datetime import datetime
from datetime import timedelta


class slackConnect():

    def __init__(self,token):
        self.token = token


    def connection(self):
        client = slack.WebClient(token=self.token, run_async = True)
        return client

class slackMessage(slackConnect):

    try:
        def __init__(self, token):
            slackConnect.__init__(self, token)
#             self.channel = channel
#             self.text = text
#             self.username = username


        def sendmessage(self, channel, text, username):
            value = slackConnect.connection(self)
            value.chat_postMessage(
                channel=channel,
                text=text,
                username=username
            )

        def schedulemessage(self, channel, text, date):
            value = slackConnect.connection(self)
            t = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            utctime = t + timedelta(hours = 8)
            timestamp=calendar.timegm(utctime.timetuple())
            value.chat_scheduleMessage(
                channel=channel,
                text=text,
                as_user=True,
                post_at=timestamp
            )

    except(e):
        print(e)
