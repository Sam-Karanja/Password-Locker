import unittest
from main import Users
from main import Credentials


class TestClass(unittest.TestCase):
    """a test class that defines test cases for the User class"""

def setUp(self):
   """method that runs befor each individual test method runss"""
    self.new_user = Users('Ogaye Mike','yuvicytr')