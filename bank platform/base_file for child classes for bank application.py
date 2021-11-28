import random
from W7_A3_Base_file_for_Parent_Class_Ednah_Akoth import BankAccount#Import the blueprint for the bank accounts
from W7_A3_Base_File_for_Functions_Ednah_Akoth import going_back #Gets the function that is called after a user is done performing a certain task to ask what action they would like to do next


random.seed(113920392049)#Change of seed number from the one set before to make sure the bank accounts being generated here are not the same as the ones before


class Current(BankAccount):#Class for current accounts (interest of 1%).. Inherits from the Parent class BankAccount
    def __init__(self, name, pin, balance, months):#Constructing the class blue print for Current Accounts
        self.months = months #Adding months to track for how long the money has been in the bank
        super(Current, self).__init__(name, pin, balance)

    def interest(self): #Calculates the interest that's added to initial amount to get the total money available in the Account After addition of interest
        # print(self.balance)
        interest = self.balance * 0.01 * self.months
        total_amt = self.balance + interest
        self.balance = total_amt #Then updates the balance in the object to show this total Money
        return self.balance #Returns the  balance

    def deposit(self):
        # print(self.balance)
        current_bal = self.interest()#Uses the method interest to calculate the current balance = Principle+Interest
        dep_amt = int(input("How much would you like to deposit? ($): "))
        self.balance = current_bal + dep_amt # This updates the balance in the object to reflect the deposit added to the current balance (Principle+Interest)
        print(f"You have added {dep_amt} to your account. Your balance is ${self.balance}")
        going_back()#asks whether they would like to go back to main menu or exit the program

    def account_details(self):#Display the account details
        # total_amount = self.interest()
        print(f"""These are the details of your Current account
                 Account holder name: {self.name}
                 Months open: {self.months}                 
                 Current amount in account: {self.balance}""")
        going_back()#asks whether they would like to go back to main menu or exit the program

    def withdraw(self):
        if self.months < 1: #Checking is the money has been in the bank less than 1 month to determine if the transaction is viable
            print(f"You can only withdraw after a month. Your money has been in the bank for {self.months} months")
            going_back()#asks whether they would like to go back to main menu or exit the program
        total_amount = self.interest()#Uses the method interest to calculate the current balance = Principle+Interest
        withdraw_amt = int(input("How much would you like to withdraw?"))
        if total_amount >= withdraw_amt:#Checks if there are enough funds to do the withdrawal
            total_amount -= withdraw_amt#If enough funds available, withdrawal amount deducted from acc
            print(f"You have withdrawn ${withdraw_amt}. Your bank account balance is ${total_amount}")
            self.balance = total_amount #Updates the balance in the object to reflect the deduction that has just occured
            going_back()#asks whether they would like to go back to main menu or exit the program
        else:
            print(f"You do not have sufficient balance. You account balance is{total_amount}")
            going_back()


class Savings(BankAccount):#Class for Savings accounts (interest of 1%).. Inherits from the Parent class BankAccount
    def __init__(self, name, pin, balance, months):#Constructing the class blue print for Savings Accounts
        self.months = months
        super(Savings, self).__init__(name, pin, balance)

    def interest(self):#Calculates the interest that's added to initial amount to get the total money available in the Account After addition of interest
        # print(self.balance)
        interest = self.balance * 0.03 * self.months
        total_amt = self.balance + interest
        self.balance = total_amt#Then updates the balance in the object to show this total Money
        return self.balance

    def deposit(self):#Code same as in Current Class
        current_bal = self.interest()
        dep_amt = int(input("How much would you like to deposit? ($): "))
        self.balance = current_bal + dep_amt
        print(f"You have added {dep_amt} to your account. Your balance is ${self.balance}")
        going_back()

    def account_details(self):#Code same as in Current Class
        print(f"""These are the details of your Current account
                         Account holder name: {self.name}
                         Months open: {self.months}
                         Current amount in account: {self.balance}""")
        going_back()


    def withdraw(self):
        if self.months < 6:#Checks if the money has been in the account for the required 6 months before withdrawal
            print(f"You cannot withdraw yet. You money has been in the bank for only {self.months} month(s)")
            going_back()#asks whether they would like to go back to main menu or exit the datab
        elif self.months >= 6:#If condition meet, user proceeds with the withdrawal
            total_amount = self.interest() #Calculates the current balance in the account inclusive of interest
            withdraw_amt = int(input("How much would you like to withdraw?"))
            if total_amount >= withdraw_amt:#Checks if there are enough funds to carry out the withdrawal
                total_amount -= withdraw_amt
                print(f"You have withdrawn ${withdraw_amt}. Your bank account balance is ${total_amount}")
                self.balance = total_amount#Updates the Objects balance to reflect the deduction
                going_back()
            else:
                print(f"You do not have sufficient balance. You account balance is{total_amount}")
                going_back()