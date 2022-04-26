import unittest
from main import Users
from main import Credentials


class TestClass(unittest.TestCase):
    """a test class that defines test cases for the User class"""

def setUp(self):
   """method that runs befor each individual test method runss"""
    self.new_user = Users('SamKaranja','yuvicytr')

 def test_init(self):
        """
        test case to chek if the object has been initialized correctly
        """
        self.assertEqual(self.new_user.username,'SamKaranja')
        self.assertEqual(self.new_user.password,'yuvicytr')