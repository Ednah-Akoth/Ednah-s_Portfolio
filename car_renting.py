#plate_number: model, year_released, year_purchased, renting_rate($), times_rented
#NB: Money made by a car has been broken down into 2: The rate of renting the car and number of times it has been rented.
    #Thus when Omondi wants to check how much a car has made, the program multiplies the rate by number of times rented
car_database = {'KAA100': ["Honda",'2015','2016', 100, 5],
                'KAB200': ['Subaru', '2017', '2018', 250, 30],
                'KAC300': ['Mercedes', '2018','2018', 300, 21],
                'KAD400': ['Lexus', '2020','2021',400,14 ],
                'KAE500': ['Toyota', '2010', '2013', 100, 9]}

valid_acceptance = ['yes', 'y']
valid_decline = ['n', 'no']

def going_back():#Since it is being repeatedly used in the program, this function has been created separately. After a user is done perfoming an action, it asks whether they would like to go back to main menu or exit the database
    ans = input("Enter 1 to go to main menu and 2 to exit the database").replace(" ", "").lower()
    if ans == '1' or ans == 'one':
        opening()

    elif ans == '2' or ans == 'two':
        exit()


def add_car():#Called when user enters 1: Add a car to your collection
    def process():#Function to allow user to add the attributes of the car
        plate_number = input('Enter the plate number of the car:').replace(" ", "").upper()#Removes any spaces the user enters and converts it to upper to match the way the plate number is stored in the dictionary
        if plate_number in car_database:#Checks if the car to be added is already in the database. If yes, takes user back to menu
            print(f"A car with plate {plate_number} already exists with the following details:{car_database[plate_number]}.\n Choose option 5 to see cars already existent in the database\n" )
            opening()
        model = input('What is the model of the car you are adding?:').capitalize()
        year_released = input("What is its year of release?:").replace(" ", "")
        year_purchased = input("In what year did you purchase this car?:").replace(" ", "")
        renting_rate = int(input("What is it's renting rate($)? enter response in numbers: "))
        times_rented = int(input("How many times has it been rented out already?enter response in number:"))
        car_database[plate_number] = [model, year_released, year_purchased, renting_rate, times_rented]#Adds all the entered values to the appropriate locations in the list.
        print("Addition successful")
    process()

    while True:
        question = input('Would you like to add another car? Yes or No?').replace(" ","").lower()  # Modifies input to match defined values of acceptance and rejections
        if question in valid_acceptance:
            process()#If the user wants to add another car, then we call the process function again
            break
        elif question in valid_decline:
            going_back()# Asks the user what they want to do next. Either go back to Main menu or exit the database. While True used to keep prompting user to key in something valid incase they don't enter a valid response
        else:
            print("Enter a valid response.")

def remove_car():#Called when user enters 2: Remove a car from your collection
    def pop_car():
        num_plate = input("Enter the number plate of the car you would like to remove:").replace(" ", "").upper()#Removes any spaces the user enters and converts it to upper to match the way the plate number is stored in the dictionary
        if num_plate not in car_database:#Checks if car is in the database. If not, user taken back to main menu
            print("There is no car with this plate number in the database. Pick option 5 in the main menu to see list of cars in the database")
            opening()
        car_database.pop(num_plate)
        print(f"Car with plate number {num_plate} removed successfully")
    pop_car()#Calls the function
    while True:
        another = input("Would you like to remove another car? Yes or No?").replace(" ","").lower()#modified to match list of accepted and not accepted values
        if another in valid_acceptance:
            pop_car() #Recalls the removing function
        elif another in valid_decline:
            going_back()# Asks the user what they want to do next. Either go back to Main menu or exit the database. While True used to keep prompting user to key in something valid incase they don't enter a valid response
        else: print("Enter a valid response")

def update_attribute(): #Called when user enters number 3:Update attributes of a car
    num_plate_of_car_to_be_updated = input("Please enter the plate number of the car you want to update:").replace(" ","").upper()#Removes any spaces the user enters and converts it to upper to match the way the plate number is stored in the dictionary
    if num_plate_of_car_to_be_updated not in car_database:  #Checks if plate entered is in the database. If not, user taken back to main menu
        print("The plate_number entered is not in the database. \n Check the list of cars available in the database by choosing option 5")
        opening()
    #This print presents the user with attributes the cars are stored with in the system
    print("""The database has the following attributes:
              1. model
              2. year_released
              3. year_purchased
              4. renting_rate($)
              5. times_rented
              """)

    while True:
        update = input("Which attribute would you like to update? Enter its corresponding number:").replace(" ", "").lower()
        if update == '1' or update == 'one': #If user wants to update Model
            print("Current value:",car_database[num_plate_of_car_to_be_updated][0])#retrieves current value to the attribute to be updated
            new_model = input('Enter new model name:').replace(" ", "").capitalize()#User input modified to match how models are stored in the dictionary
            car_database[num_plate_of_car_to_be_updated][0] = new_model
            print(f"These are now the attributes of the car arranged in the following order [model, year_released, year_purchased, renting_rate($), times_rented]\n:{car_database[num_plate_of_car_to_be_updated]}")
            break
        elif update == "2" or update == "two":#If user wants to update year_released
            print("Current value:",car_database[num_plate_of_car_to_be_updated][1])
            new_year = input('Enter new year of release value:').replace(" ", "")#Spaces removed to maintain uniformity
            car_database[num_plate_of_car_to_be_updated][1] = new_year
            print(f"These are now the attributes of the car arranged in the following order [model, year_released, year_purchased, renting_rate($), times_rented]\n:{car_database[num_plate_of_car_to_be_updated]}")
            break

        elif update == '3' or update == "three": #If user wants to update year_purchased
            print("Current value:", car_database[num_plate_of_car_to_be_updated][2])
            year_pur = input('Enter new year of purchase value:').replace(" ", "")
            car_database[num_plate_of_car_to_be_updated][2] = year_pur
            print(f"These are now the attributes of the car arranged in the following order [model, year_released, year_purchased, renting_rate($), times_rented]\n:{car_database[num_plate_of_car_to_be_updated]}")
            break

        elif update =="4" or update =="four":#If user wants to update renting_rate($)
            print("Current value:", car_database[num_plate_of_car_to_be_updated][3])

            rent_rate = int(input("Enter the new renting rate:"))
            car_database[num_plate_of_car_to_be_updated][3] = rent_rate
            print(f"These are now the attributes of the car arranged in the following order [model, year_released, year_purchased, renting_rate($), times_rented]\n:{car_database[num_plate_of_car_to_be_updated]}")
            break

        elif update == "5" or update =="five":#If user wants to update the number of times a car has been rented
            print("Current number of times rented:", car_database[num_plate_of_car_to_be_updated][4])

            times_rented = int(input("Enter the new number of times rented:"))
            car_database[num_plate_of_car_to_be_updated][4] = times_rented
            print(f"These are now the attributes of the car arranged in the following order [model, year_released, year_purchased, renting_rate($), times_rented]\n:{car_database[num_plate_of_car_to_be_updated]}")
            break

        else: print("Enter a valid response")


    while True:
            finishing_qn = input('Would you like to update another car? Yes or No?').replace(" ","").lower()
            if finishing_qn in valid_acceptance:
                update_attribute() #If they want to update another car, the update function is recalled
                break
            elif finishing_qn in valid_decline:
                going_back() # Asks the user what they want to do next. Either go back to Main menu or exit the database. While True used to keep prompting user to key in something valid incase they don't enter a valid response

            else:
                print("Enter a valid response.")

def money_made(): #Called when user enters option 4: Calculate amount made from renting a certain car

    plate = input("Please enter the plate number of the car you want to calculate money made for:").replace(" ","").upper()
    if plate not in car_database:#Checks if car is in the database. If not, user taken back to main menu
        print("There is no car with this plate number in the database. Pick option 5 in the main menu to see list of cars in the database")
        opening()
    rent_rate = car_database[plate][3]#Stores rent rate of the car specified by user
    no_of_times_rented = car_database[plate][4] #Stores number of times car has been rented for the car specified by user
    amount_made = rent_rate * no_of_times_rented #Multiplies rate by no of times rented to find amount made
    print(f"The amount made from renting this car so far is ${amount_made}")


    while True: #If user wants to calculate money for another car, it calls the asking user function again, if not, it calls the going back function. Ensures user enters a valid answer
        resp = input("Would you like to calculate money made for another car? Yes or No?").replace(" ","").lower()
        if resp in valid_acceptance:
            money_made()
            break
        elif resp in valid_decline:
            going_back() #This gives the user two options. To either go to main menu or exit database
        else: print("Enter a valid response")


def view_database(): # This function is called when user enters number 5. Shows user all cars in the dictionary as well as the total amount made by the cars
    print("""The values are arranged in the following sequence:
    plate_number: [model, year_released, year_purchased, renting_rate($), times_rented]""")
    print(car_database)

    #This next part shows Omondi how much he has made so far from renting out all his cars
    rent_rate = [] #List to hold the rent rates of each car
    times_rented = [] #List to hold the # of times cars have been rented
    total_resp_amounts = [] #List that holds total amount made by each car (calculated by multiplying a value in rent_rate by its respesctive value in times_rented
    for car in car_database: # This will iterate through the dictionary add the rent rates and no of times rented to respective lists
        rent_rate.append(car_database[car][3])
        times_rented.append(car_database[car][4])
    for r,t in zip(rent_rate,times_rented): #This loop multiplies a value in rent_rate by its respesctive value in times_rented
            total_resp_amounts.append(r * t)
    total_money_made = sum(total_resp_amounts)#Adds the money made by each car
    print(f'Total amount made by renting all your cars thus far:${total_money_made}')


    while True:
        going_back()# Asks the user what they want to do next. Either go back to Main menu or exit the database. While True used to keep prompting user to key in something valid incase they don't enter a valid response


#presenting the user with options:
def opening():
    print("""Welcome to your car database system. What action would you like to perform?
             1. Add a car to your collection
             2. Remove a car from your collection
             3. Update attributes of a car (updating the number of times a car has been rented, model, year released, year purchased, renting rate)
             4. Calculate amount made from renting a certain car            
             5. View entire database of cars
            
             """)
    while True:
        response = input("Enter the number that corresponds to the action desired:").strip() #Takes user's response,removes any leading or trailing spaces to ensure that regardless of how the number is entered it is the same as what is compared with
        #Checks the users response and maps responses to the appropriate program segments by calling the respective functions
        if response == '1':
            add_car()
            break
        elif response == '2':
            remove_car()
            break
        elif response == '3':
            update_attribute()
            break
        elif response =='4':
            money_made()
            break
        elif response == '5':
            view_database()
            break
        else:
            print("Please enter a valid response")

opening() #Calls the function that opens the user to the database


