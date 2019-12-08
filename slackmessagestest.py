
# coding: utf-8

# In[1]:


import unittest #import unittest
from webcommunication.slack.slackmessage import *
class TestSlackMessage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupClass')
    def setUp(self):
        self.p2=slackMessage("****tokenhere****","Test Channel","Hello","User","2019-12-05 23:00:00")
        self.p2.sendmessage('Test Channel','Hello','User')
        print("setUp")
    
    def test_sendmessage(self):
        #p2=slackMessage("token","Test Channel","Hello","User","2019-12-05 23:00:00")
        #p2.sendmessage('Test Channel','Hello','User')
        self.assertEqual(self.p2.channel,'Test Channel')
        self.assertIs(self.p2.text,'Hello')
        self.assertIsNot(self.p2.username,'Test2')
        self.assertIsNotNone(self.p2.channel)
        self.assertNotEqual(self.p2.text,'Test3')
    
    def test_schedulemessage(self):
         #p2=slackMessage("token","Test Channel","Hello","User","date")
         #p2.schedulemessage('Test Channel','Hello','User')
        self.assertEqual(self.p2.channel,'Test Channel')
        self.assertIs(self.p2.text,'Hello')
        self.assertIsNot(self.p2.username,'Test2')
        self.assertIsNotNone(self.p2.channel)
        self.assertNotEqual(self.p2.text,'Test3')
        self.assertEqual(self.p2.date,'2019-12-05 23:00:00')
    @classmethod
    def tearDownClass(cls):
        print('teardownClass')
    def tearDown(self):
        print('teardown')
unittest.main(argv=[''],verbosity=2,exit=False)


# **We are getting the above error because of Slack API call and we are testing it with a mock token instead of a confidential legacy token**
