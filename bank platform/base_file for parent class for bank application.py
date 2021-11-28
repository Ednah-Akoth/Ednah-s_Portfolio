
from W7_A3_Base_File_for_Functions_Ednah_Akoth import user_accounts #Dictionary that stores the objects
from W7_A3_Base_File_for_Functions_Ednah_Akoth import bank_account_numbers#List that stores bank accounts randomly generated
from W7_A3_Base_File_for_Functions_Ednah_Akoth import going_back #Function that displays options after a user is done with an action
from W7_A3_Base_File_for_Functions_Ednah_Akoth import intro#Function that gives the user menu options
import random
class BankAccount:

    def __init__(self,name,pin,balance): #Constructing the class blue print
        self.name = name
        self.pin = pin
        self.balance = balance
        self.acc_num = random.randrange(10 ** 12, 10 ** 13) #Generates a random number for the bank accounts that are created
        bank_account_numbers.append(self.acc_num)#Since the numbers are being randomly generated, this list helps to know what the
        # bank accounts are for the purposes of testing the code.

    def deposit(self):
        # deposit(self)
        dep_amt = int(input("How much would you like to deposit? ($): ")) #Asks user for amt and converts to int
        self.balance += dep_amt #Updates the balance attribute to reflect the addition in money
        print(f"You have added {dep_amt} to your account. Your balance is ${self.balance}")
        going_back() #Asks the user whether they want to perform another action or leave the application

    def withdraw(self):
        withdraw_amt = int(input("How much would you like to withdraw?"))
        if self.balance >= withdraw_amt:#Checks whether the balance is greater than the amt to be withdrawn
            self.balance -= withdraw_amt #Updates the balance attribute by deducting the amount being withdrawn
            print(f"You have withdrawn ${withdraw_amt}. Your bank account balance is ${self.balance}")
            going_back()#Asks the user whether they want to perform another action or leave the application
        else:
            print(f"You do not have sufficient balance. You account balance is{self.balance}")#If the user doesn't have enough funds, they are told as such and their balance is displayed to them
            going_back()#Asks the user whether they want to perform another action or leave the application
####______________________________________________________________________________________________________________-
    def transfer(self):#To tranfer money from one user to another
        transfer_amt = int(input("How much would you like to transfer($)?:"))
        if self.balance >= transfer_amt: #Checks if the sender has enough money to perform the transaction
            other_acc = int(input("Enter the bank account you would like to transfer money to: ")) #User entered acc that money is being transferred to
            if other_acc == self.acc_num: #Transfers cannot happen within the same account. A user cannot send money to their own account
                print("You cannot transfer money to your own account")
                going_back()#Asks the user whether they want to perform another action or leave the application
            if other_acc not in user_accounts:#Checks if the account entered exists
                print(f"The bank account {other_acc} does not exist. Confirm the account number and try again")
                intro()#Takes user back to menu options

            self.balance -= transfer_amt #Deducting the amt from sender's account
            user_accounts[other_acc].balance += transfer_amt #Crediting the money to recipients account
            print(f"You have transferred {transfer_amt} to user with bank account {other_acc}.\nYour balance is {self.balance}")#Shows the user how much they've transferred, to which account and their balance
            going_back()#Asks the user whether they want to perform another action or leave the application
        else:#If user doesn't have enough money to transfer
            print("You do not have sufficient funds to transfer that amount. Your current balance is $",self.balance)
            going_back()#Asks the user whether they want to perform another action or leave the application
#####______________________________________________________________________________________________________________-

    def account_details(self):#Prints out the account details of the user:Their name, account number and bank balance.
        print(f"""Your account details are as follows:
                 Account holder's name = {self.name}
                 Account number = {self.acc_num}
                 Account balance = {self.balance}""")
        going_back()#Asks the user whether they want to perform another action or leave the application
