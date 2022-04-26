import random
import string


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
    




