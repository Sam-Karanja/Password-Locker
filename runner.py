from main import Users, Credentials


def create_new_user(username, password):
    """function to create a new user from the user class with username and password"""
    new_user = Users(username, password)
    return new_user

def save_user(user):
    """function to save a new user"""
    user.adduser()

def display_user():
    """funtion to display an existing user"""
    return Users.display_user()

def login_user(username,password):
    """function that allows an existiny user to  login"""
    check_user = Credentials.verify_user(username, password)
    return check_user

def create_new_credential(account,userName,password):
    """function that create new credentials for a given user account"""
    new_credential = Credentials(account, userName, password)
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


def generate_Password():
    '''
    generates a random password for the user.
    '''
    auto_password=Credentials.generatePassword()
    return auto_password
def copy_password(account):
    """
    A funct that copies the password using the pyperclip framework
    We import the framework then declare a function that copies the emails.
    """
    return Credentials.copy_password(account)


def permissoner():
    print(" Welcome Dear Subscriber ...\n Enter one of the following to proceed.\n ca ---  Create New Account  \n li ---  already have account?  \n")
    short_code=input("").lower().strip()
    if short_code == "ca":
        print("Sign Up")
        print('-' * 60)
        username = input("Provide userName: ")
        while True:
            print(" TP - To type your own pasword:\n GP - To generate random Password")
            password_Choice = input().lower().strip()
            if password_Choice == 'tp':
                password = input("Enter Password\n")
                break
            elif password_Choice == 'gp':
                password = generate_Password()
                break
            else:
                print("Invalid password please try again")
        save_user(create_new_user(username,password))
        print("*"*85)
        print(f"Hello {username}, Your account has been created succesfully! Your password is: {password}")
        print("*"*85)
    elif short_code == "li":
        print("*"*70)
        print("Enter your User name and your Password to log in:")
        print('*' * 70)
        username = input("User name: ")
        password = input("password: ")
        login = login_user(username,password)
        if login_user == login:
            print(f"Hello {username}.Welcome To Our Application")  
            print('\n')
    while True:
        print("Use these short codes:\n CC - Create a new credential \n DC - Display Credentials \n FC - Find a credential \n GP - Generate A randomn password \n D - Delete credential \n EX - Exit the application \n")
        short_code = input().lower().strip()
        if short_code == "cc":
            print("Create New Credential")
            print("."*20)
            print("Account name ....")
            account = input().lower()
            print("Your Account username")
            userName = input()
            while True:
                print(" TP - To type your own pasword if you already have an account:\n GP - To generate random Password")
                password_Choice = input().lower().strip()
                if password_Choice == 'tp':
                    password = input("Enter Your Own Password\n")
                    break
                elif password_Choice == 'gp':
                    password = generate_Password()
                    break
                else:
                    print("Invalid password please try again")
            save_credentials(create_new_credential(account,userName,password))
            print('\n')
            print(f"Account Credential for: {account} - UserName: {userName} - Password:{password} created succesfully")
            print('\n')
        elif short_code == "dc":
            if display_user():
                print("Here's your list of acoounts: ")

                print('*' * 30)
                print('_'* 30)
                for account in display_user():
                    print(f" Account:{account.account} \n User Name:{username}\n Password:{password}")
                    print('_'* 30)
                print('*' * 30)
            else:
                print("You don't have any credentials saved yet..........")
        elif short_code == "fc":
            print("Enter the Account Name you want to search for")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"Account Name : {search_credential.account}")
                print('-' * 50)
                print(f"User Name: {search_credential.userName} Password :{search_credential.password}")
                print('-' * 50)
            else:
                print("That Credential does not exist")
                print('\n')
        elif short_code == "d":
            print("Enter the account name of the Credentials you want to delete")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("_"*50)
                search_credential.delete_credentials()
                print('\n')
                print(f"Your stored credentials for : {search_credential.account} successfully deleted!!!")
                print('\n')
            else:
                print("That Credential you want to delete does not exist in your store yet")

        elif short_code == 'gp':

            password = generate_Password()
            print(f" {password} Has been generated succesfull. You can proceed to use it to your account")
        elif short_code == 'ex':
            print("Thanks for using Password_Locker.. See you next time!")
            break
        else:
            print("Wrong entry... Check your entry again and let it match those in the menu")
    else:
        print("Please enter a valid input to continue")

if __name__ == '__main__':
    permissoner()