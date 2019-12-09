
# coding: utf-8

# In[5]:


import unittest
from emailsimpletest import TestEmailSimple
from emailadvancedtest import TestEEmailAdv
from slackmessagestest import TestSlackMessage
from slackchanneltest import TestSlackChannel

def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestEmailSimple))
    suite.addTest(unittest.makeSuite(TestEEmailAdv))
    suite.addTest(unittest.makeSuite(TestSlackMessage))
    suite.addTest(unittest.makeSuite(TestSlackChannel))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))

my_suite()

