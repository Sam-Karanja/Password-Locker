import unittest
from main import Users
from main import Credentials


class TestClass(unittest.TestCase):
    """a test class that defines test cases for the User class"""

def setUp(self):
    """method that runs befor each individual test method runss"""
    self.new_user = Users('SamKaranja','skmurigi')

    def test_init(self):
        """
        test case to chek if the object has been initialized correctly
        """
        self.assertEqual(self.new_user.username,'SamKaranja')
        self.assertEqual(self.new_user.password,'yuvicytr')

    def test_save_user(self):
        """
        test case to test if a new user instance has been saved into the User list
        """
        self.new_user.adduser()
        self.assertEqual(len(Users.user_list),1)

class TestCreds(unittest.TestCase):
    """
    A test class that defines test cases for credentials class
    """ 
    def setUp(self):
        """
        Method that runs before each individual credentials test methods run.
        """
        self.new_credential = Credentials('facebook','Sam Karanja','beaut56')
    def test_init(self):
        """
        Test case to check if a new Credentials instance has been initialized correctly
        """
        self.assertEqual(self.new_credential.account,'facebook')
        self.assertEqual(self.new_credential.userName,'Sam Karanja')
        self.assertEqual(self.new_credential.password,'beaut56')


    def save_credential_test(self):
        """test case to test if the credential object is saved into the credential list"""
        self.new_credential.save_details()
        self.assertEqual(len(Credentials.credslist),1)

    def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        Credentials.credslist = []

    def test_save_many_accounts(self):
        '''
        test to check if we can save multiple credentials objects to our credentials list
        '''
        self.new_credential.save_details()
        test_credential = Credentials("pintrest","ugavmic","laton3") 
        test_credential.save_details()
        self.assertEqual(len(Credentials.credslist),2)

    
    def test_delete_credential(self):
        """
        test method to test if we can remove an account credentials from our credentials_list
        """
        self.new_credential.save_details()
        test_credential = Credentials("pintrest","ugavmic","laton3")
        test_credential.save_details()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credslist),1)

    def test_find_credentialr(self):
        """
        test to check if we can find a credential entry by account name and display the details of the credential
        """
        self.new_credential.save_details()
        test_credential = Credentials("pintrest","ugavmic","laton3") 
        test_credential.save_details()

        new_credential = Credentials.find_credential("Twitter")

        self.assertEqual(new_credential.account,test_credential.account)