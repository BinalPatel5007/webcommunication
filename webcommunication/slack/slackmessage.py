
# coding: utf-8

# In[4]:


import slack
import calendar
from datetime import datetime
from datetime import timedelta
import schdate


class slackConnect():
    
    def __init__(self,token):
        self.token = token
    
    
    def connection(self):
        client = slack.WebClient(token=self.token, run_async = True)
        return client    

class LongStringError(Exception): 
    def __init__(self):
        print("text too long")
        
class ShortStringError(Exception): 
    def __init__(self):
        print("text too short")
        
class slackMessage(slackConnect):
    
    try:
        def __init__(self, token):
            slackConnect.__init__(self, token,channel,text,username,date)
            self.channel = channel
            self.text = text
            self.username = username

        def sendmessage(self, channel, text, username):
            try:
                if len(text) >= 10:
                    raise LongStringError
                elif len(text) <= 5:
                    raise ShortStringError
                else:        
                    value = slackConnect.connection(self)
                    value.chat_postMessage(
                        channel=channel,
                        text=text,
                        username=username
                    )
            except LongStringError:
                print("Reduce the number of characters in the text")
            except ShortStringError:
                print("Increase the number of characters in the text")
            except e:
                print("Exceptional Error")
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
        


# In[3]:




