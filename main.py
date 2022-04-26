import random
import pyperclip

from click import password_option


class Users:

   user_list = []
   def __init__(self,username,password):

        self.username=username
        self.password=password

   def adduser (self):
      self.user_list.append(self)

   
   @classmethod
   def display_user(cls):
       return cls.user_list

   def delete_user(self):
       Users.user_list.remove(self)


class Credentials:
    
    @classmethod
    def verify_user(cls, username, password):
        """method to verify whether the user is in our list or not"""

        a_user = ""
        for user in Users.user_list:
            if(user.username == username and user.password == password):
                a_user == user.username
        return a_user

    def __init__(self,account, username,passoword):
        """instantiation of the credentials class object"""
        
        self.accout = account
        self.userName = username
        self.password = password


    def save_details(self):
        """method to store a new credential to the credslist"""

        Credentials.credslist.append(self)


    def delete_details(self):
        """removes the user's credentials when called"""

        Credentials.credslist.remove(self)

        
@classmethod
def find_credentials(cls, account):
    """method that takes in the account name and returns the account credetials"""
    
    for cred in cls.credslist:
        if cred.account == account:
            return cred

@classmethod
def copy_password(cls, account):
    found_credentials = Credentials.find_credential(account)
    pyperclip.copy(found_credentials.password)

@classmethod
def check_credential(cls, account):
    """method that checks whether a credential exists in the credential list and returns true or false"""
    for credential in cls.credentials_list:
        if credential.account == account:
            return True
        return False





