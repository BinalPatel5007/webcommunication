#!/usr/bin/env python
# coding: utf-8

# In[3]:


from webcommunication.slack import slackchannel
from webcommunication.slack import slackmessage


# In[4]:


c = slackchannel.slackChannel("*****")
c.createchannel('testChannel')


# In[10]:


m = slackmessages.slackMessage("******")
m.sendmessage("testChannel", "Hello", "USER")
m.schedulemessage("testChannel", "Hello", "2019-11-29 12:43:00")


# In[1]:


import webcommunication
from webcommunication.email import emailsimple


# In[2]:


emailsimple.emailsend("*****@gmail.com", "******","Test Email Subject","Hello, Test Message","*****@gmail.com", "****@gmail.com")


# In[3]:


from webcommunication.email import emailadvanced


# In[5]:


emailadvanced.emailsendattach("*****@gmail.com","*****@gmail.com", "Email from Python", "*****", "Hello", "Data533_ProjectProposal.pdf")


# In[ ]:




