
from W7_A3_Base_File_for_Functions_Ednah_Akoth import user_accounts #Imports the database to store objects
from W7_A3_File_For_Child_Classes_Ednah_Akoth import Current #Imports the child class
from W7_A3_File_For_Child_Classes_Ednah_Akoth import Savings#Imports the child class
from W7_A3_Base_File_for_Functions_Ednah_Akoth import entry #To get the function that asks user for log in credentials
##Use the following bank accounts and Pins for testing
##Current_Account Bank account numbers: [Neema Akoth = 3650303816885 Pin = 1234], [Juma Shaheed = 4056956542525 Pin= 5678],
# [Ahmed Bashir = 6020864816674 Pin= 2345], [Andrew Turi = 6961142901614 Pin = 3765], Waruri Anzar = 9749299021234 Pin=5389]

c7 = Current("Neema Akoth",1234, 500000,0.25)#Creating an object of the Current class
user_accounts[c7.acc_num] = c7#Appending the object to the dictionary using their bank account number as the key and the object as the value
c8 = Current("Juma Shaheed",5678,9000000,0.5)
user_accounts[c8.acc_num] = c8
c9 = Current("Ahmed Bashir", 2345, 7000000,1)
user_accounts[c9.acc_num] = c9
c10 = Current("Andrew Turi", 3765, 7000000,1.5)
user_accounts[c10.acc_num] = c10
c11 = Current("Waruri Anzar", 5389, 7000000,1.5)
user_accounts[c11.acc_num] = c11
##Savings Account Bank Account Numbers:[ Jimmy Wanjigi = 1734582538590 Pin = 8765],
# [Allan Marie = 5993853844070 Pin = 7468], [Paul Johnson = 5549823104542 Pin = 3489]
c12 = Savings("Jimmy Wanjigi",8765,1000000,1)#Creating an object of the Savings class
user_accounts[c10.acc_num] = c10

c13 = Savings("Allan Marie",7468,200,6)
user_accounts[c11.acc_num] = c11

c14 = Savings("Paul Johnson",3489,60000,20)
user_accounts[c12.acc_num] = c12

entry()#Calling the function that will start the log in process
# print(bank_account_numbers)