
#This file contains objects of the BankAccount class.
from W7_A3_Base_File_for_Functions_Ednah_Akoth import entry #To get the function that asks user for log in credentials
from W7_A3_Base_File_for_Functions_Ednah_Akoth import user_accounts #Dictionary to store the objects in
from W7_A3_Base_file_for_Parent_Class_Ednah_Akoth import BankAccount #Import the blueprint for the bank accounts
#Use the following bank accounts and PINs to log in
##Bank account numbers [Ednah Akoth = 7982283635038 Pin = 9876], [Sabaahat Shaheed = 9545409840963 Pin = 7487], [Amreen Bashir = 1822401110318 Pin =2724]
# [Nancy Ishimwe = 9695110959589 Pin = 2380], [John Ganda = 1743880875493 Pin=7869], [James Nyamo =3386651395857, Pin = 4390]
c1 = BankAccount("Ednah Akoth",9876, 500000) #Creating Objects of the class
user_accounts[c1.acc_num] = c1 #Appending the object to the dictionary using their bank account number as the key and the object as the value
c2 = BankAccount("Sabaahat Shaheed",7487,9000000)
user_accounts[c2.acc_num] = c2
c3 = BankAccount("Amreen Bashir", 2724, 7000000)
user_accounts[c3.acc_num] = c3
c4 = BankAccount("Nancy Ishimwe", 2380, 0)
user_accounts[c4.acc_num] = c4
c5 = BankAccount("John Ganda",7869, 100)
user_accounts[c5.acc_num] = c5
c6 = BankAccount("James Nyamo", 4390, 75000)
user_accounts[c6.acc_num] = c6



entry()#Calls the login function to start the program


