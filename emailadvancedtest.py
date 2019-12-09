
# coding: utf-8

# In[3]:


#create a test class by inheriting unittest.testcase
import unittest
from webcommunication.email import emailadvanced
class TestEEmailAdv(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupClass')
    def setUp(self):
        print("setUp")
        self.t2=emailadvanced.emailsendattach('dummytest533@gmail.com',
                                 'dummytest533@gmail.com',
                                 'Test email subject',
                                'Data533!',
                                'This is a test email',
                                'ISLR Seventh Printing.pdf')
        #print(self.t2)

    def test_emailsendattach(self):
# #        self.assertEqual(emailsimple.emailsend("dummytest533@gmail.com","Data533!","Test email subject","This is a test email","dummytest533@gmail.com","sneha.mikkilinenidurga@gmail.com"),"dummytest533@gmail.com" "Data533!" "Test email subject" "This is a test email" "dummytest533@gmail.com" "sneha.mikkilinenidurga@gmail.com")
        self.assertIs(self.t2,None)
# #         self.assertIsNot(self.t2.content,'Hello')
        self.assertIsNone(self.t2)
# #         self.assertNotEqual(self.t2.password,'abc')
    @classmethod
    def tearDownClass(cls):
        print('teardownClass')
    def tearDown(self):
        print('teardown')

unittest.main(argv=[''],verbosity=2,exit=False)

