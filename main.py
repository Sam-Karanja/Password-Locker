import random
import string

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
        
        





