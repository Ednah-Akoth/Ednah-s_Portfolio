import random

user_accounts = {} #A dictionary to store a user accounts as they are created
random.seed(100000000) #Seed number set to make sure the bank account numbers generated don't change when the code is rerun
bank_account_numbers = [] #List to store the bank account numbers that are being randomly generated

def going_back():#Since it is being repeatedly used in the program, this function has been created separately. After a user is done perfoming an action, it asks whether they would like to go back to main menu or exit the database
    while True:
        ans = input("Enter 1 to go to main menu and 2 to exit the application").replace(" ", "").lower()
        if ans == '1' or ans == 'one':
            intro()
        elif ans == '2' or ans == 'two':
            exit()
        else:
            print("Enter a valid response please")
def entry():#Function that asks the user for their login credentials
    while True:
        global bank_account#This variable will be used later to call methods of the classes. Since its defined localy and needs to be used globally, global is used
        print("Welcome to The Dangote Bank, the leading banking service in Africa.")
        print("Enter your log in credentials")
        bank_account = int(input("Enter your bank account:"))
        passcode = int(input("Enter your pin:"))
        if bank_account in user_accounts and user_accounts[bank_account].pin == passcode:#Checks whether the bank account entered exists in the dictionary user_accounts and whether the passcode matches the preset one
            intro()#Presents user with menu of actions that can be performed
        else:
            print("Invalid bank account number or PIN")
def intro():#Presents user with menu of actions that can be performe
    try:
        print(""" What action would you like to perform?          
                    1. Deposit Money
                    2. Withdraw Money
                    3. View Balance
                    4. Transfer Money to another account         
        """)
        choice = int(input("Enter the corresponding number for desired action from the list below:"))
    except ValueError:
        print("Enter a valid response. Only enter the corresponding number")
    ##Checking the users response and matching it the appropriate response.

    if choice == 1:
        user_accounts[bank_account].deposit()#Traces the object from the dictionary using the bank account number which is the key, then calls the relevant method from the Class BankAccount
    elif choice == 2:
        user_accounts[bank_account].withdraw()
    elif choice == 3:
        user_accounts[bank_account].account_details()
    elif choice == 4:
        user_accounts[bank_account].transfer()
