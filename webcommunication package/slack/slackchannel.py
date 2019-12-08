#!/usr/bin/env python
# coding: utf-8

# In[38]:


import slack

class slackChannel():

    def __init__(self,token):
        self.token = token

    def connection(self):
        client = slack.WebClient(token=self.token, run_async = True)
        return client

    def createchannel(self, channelname):
        value = slackChannel.connection(self)
        value.groups_create(
            name=channelname
        )
