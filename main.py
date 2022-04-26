import random
import string


class Users:

   users=[]
   def __init__(self,username,password):

        self.username=username
        self.password=password

   def adduser (self,user):
       if user not in  self.users:
        self.users.append(user)


user= input('Enter your user name:')
password=input('Enter your password:')
user1=Users(user,password)
print(user1.password)
print (user1.username)
user1.adduser(user)
print(user1.users) 