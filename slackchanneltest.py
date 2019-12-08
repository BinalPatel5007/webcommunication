
# coding: utf-8

# In[1]:


import unittest 
from webcommunication.slack.slackchannel import *

class TestSlackChannel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupClass')
    def setUp(self):
        self.p1=slackChannel("****tokenhere****")
        self.channelname="Test Channel"
        print("setup")
    def test_connection(self):
        self.assertEqual(self.p1.token,"****tokenhere****")
        self.assertTrue("****tokenhere****")
        self.assertEqual(len(self.p1.token),17)
        self.assertIsNot(self.p1.token,"xoxo")
        self.assertIsNotNone(self.p1.token)
    def test_createchannel(self):
        #p1=slackChannel("xoxp-740210726487-734794619889-862295410485-22842453cfcb0f1a36183234dcf8c76c")
        #p1.createchannel("Test Channel")
        self.assertEqual(self.channelname,'Test Channel')
        self.assertTrue(self.channelname)
        self.assertIsNot(self.channelname,'Test6')             
        self.assertIsNotNone(self.channelname)
        self.assertNotEqual(self.channelname,'Test4')
    @classmethod
    def tearDownClass(cls):
        print('teardownClass')
    def tearDown(self):
        print('teardown')
unittest.main(argv =[''], verbosity=2, exit=False)


# In[8]:


# import unittest 
# from webcommunication.slack.slackchannel import *

# class TestSlackChannel(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.p1=slackChannel("****tokenhere****")
#         cls.channelname="Test Channel"
#         print('setupClass')
#     def setUp(self):
#         print(self.p1)
#         print(self.channelname)
#         print("setup")
#     def test_connection(self):
#         self.assertEqual(self.p1.token,"****tokenhere****")
#         self.assertTrue("****tokenhere****")
#         self.assertEqual(len(self.p1.token),17)
#         self.assertIsNot(self.p1.token,"xoxo")
#         self.assertIsNotNone(self.p1.token)
#     def test_createchannel(self):
#         #p1=slackChannel("xoxp-740210726487-734794619889-862295410485-22842453cfcb0f1a36183234dcf8c76c")
#         #p1.createchannel("Test Channel")
#         self.assertEqual(self.channelname,'Test Channel')
#         self.assertTrue(self.channelname)
#         self.assertIsNot(self.channelname,'Test6')             
#         self.assertIsNotNone(self.channelname)
#         self.assertNotEqual(self.channelname,'Test4')
#     @classmethod
#     def tearDownClass(cls):
#         print('teardownClass')
#     def tearDown(self):
#         print('teardown')
# unittest.main(argv =[''], verbosity=2, exit=False)

