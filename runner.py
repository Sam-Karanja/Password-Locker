from main import Users, Credentials


def create_new_user(username, password):
    """function to createa a new user from the user class with username and password"""
    new_user = Users(username, password)
    return new_user

def save_user(user):
    """function to save a new user"""
    user.save_user()

def display_user():
    """funtion to display an existing user"""
    return Users.display_user()

def login_user(username,password):
    """function that allows an existiny user to  login"""
    check_user = Credentials.verify_user(username, password)
    return check_user

def create_new_credential():
    """function that create new credentials for a given user account"""
    new_credential = Credentials(account, username, password)
    return new_credential

def save_credentials(credentials):
    """function to save user credentials to the credentials list"""
    credentials.save_details()

def display_account_details():
    """functiont that returns all the saved credentials"""
    return Credentials.display_credentials()

def delete_credentials():
    """function to delete credentials from credentials list"""
    Credentials.delete_credentials()

def find_credential(account):
    """function that finds a credential by an account name and returns the credentials that belong to that account"""
    return Credentials.find_credential(account)

def check_credential(account):
    """function that checks whether a credential exists with that account name and returns true or falsse"""
    return Credentials.check_credential_exist(account)
