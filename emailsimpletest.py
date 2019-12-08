
# coding: utf-8

# In[23]:


#create a test class by inheriting unittest.testcase
import unittest
from webcommunication.email import emailsimple
class TestEmailSimple(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupClass')
    def setUp(self):
        print("setUp")
        self.t1=emailsimple.passwordencrpt('Data533!')
        #print(self.t1)
        self.t2=emailsimple.emailsend('dummytest533@gmail.com',
                                 'Data533!',
                                 'Test email subject',
                                'This is a test email',
                                'dummytest533@gmail.com',
                                'sneha.mikkilinenidurga@gmail.com')
        #print(self.t2)
    
    def test_passwordencrpt(self):
        self.assertEqual(self.t1,b'RGF0YTUzMyE=') #'password' is getting encoded to 'b'KipwYXNzd29yZCoq'' 
        self.assertIsNot(self.t1,b'RGF0YTUzMyE=')
        self.assertIsNotNone(self.t1)
        self.assertNotEqual(self.t1,b'RGF0YTUzMyE')
        self.assertTrue(self.t1)

    def test_emailsend(self):
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


# **Our dummytest533@gmail.com is able to send and receive emails and is able to reply to sneha.mikkilinenidurga@gmail.com but we were only able to use two assert methods because the function emailsend returns None.**
