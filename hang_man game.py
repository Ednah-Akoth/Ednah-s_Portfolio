
#List of valid responses to be used in various functions in the code
valid_acceptance = ['yes', 'y']
valid_decline = ['n', 'no']
#Checks if response is valid
def checking_consent():
    # Introducing the player to the game
    print('''
    Hello ALU student! Welcome to the game of hangman that tests your knowledge of your school!
    The rules are simple. I will ask you 10 questions about ALU. Each time you miss a question, you are hanging your man!
    If you miss 6 questions,your man dies and the game ends. If you answer all the questions right, your man lives and you win!
    Remember, any invalid input counts as a wrong answer so be careful and follow instructions.''')
    # Asking the user for consent
    while True:
        response = input('Are you ready to play? Yes or No?:').replace(" ","").lower()
        consent = response.replace(" ", "")
        if consent in valid_acceptance:
            print("Let's get started!")
            break
        elif consent in valid_decline:
            print("Bye then")
            exit()
        else:
            print('That is not a valid response. Please try again.')
#Now calling the function to ask user for permission to proceed

checking_consent()



#Defining variables to be used in the game
game_over_count = 0 #Counts the number of games failed
false_answer_count = 0 #Counts the number of false answers per game played. Reset aat various points to ensure false answer count is not carried forward from one game to another
game_count = 1 #Counts number of games played. Initialised to one to account for the first game that the user will play.

#Defining functions to be used in the game
def repeat_game():#Function that asks the user whether they want to repeat the game
    global game_count,game_over_count
    while True:

        response = input("Would you like to play again? Yes or No?").replace(" ","").lower()
        if response in valid_acceptance:
            game_count += 1
            hangman_game()

        elif response in valid_decline:
            #game_over_count in game_over function is the number of games failed by user
            print(f"You have played {game_count} games, won {game_count - game_over_count} game(s) and lost {game_over_count} game(s)")
            exit()
        else:
            print("Enter a valid response")

def game_over():
    #Every time a user fails, this function adds up the game_over_count(keeps tabs of games failed)
    global game_over_count,false_answer_count#Tells python not to view the game_over_count formula as an assignment operator so that it does not throw a " local variable 'x' referenced before assignment" error
    if false_answer_count == 6:
        print("Your man is dead! Game Over!")
        game_over_count +=1
        false_answer_count = 0 # this resets the number of false answers counted so that the number of false answers is not carried over.
        repeat_game()

def hangman_game():
    global false_answer_count,game_over_count
# Question 1
    answer1 = input("Question 1: When was ALU founded? Write the year in number please(YYYY):").replace(" ", "")
    if answer1 == '2015':
        print("Welldone!")

    else:
        false_answer_count += 1
        print(f"Incorrect. You are hanging your man. your false answer count is {false_answer_count}")

    # Question 2
# Convert the input to lowercase, then remove all spaces to attain uniformity despite user's input
    answer2 = input("Question 2: Who is the CEO of ALU? Write the person's first two names(first and last):").lower().replace(" ", "")
    if answer2 == "fredswaniker" or answer2 == 'swanikerfred':
        print("Correct! Next Question.")
    else:
        false_answer_count += 1
        print(f"Incorrect. You are hanging your man. your false answer count is {false_answer_count}")

    # Question 3
    # Convert the input to lowercase, then remove all spaces to attain uniformity despite user's input
    answer3 = input("Question 3: Where are ALU campuses?(Let your answer be comma separated):").lower().replace(" ", "")
    if answer3 == "rwanda,mauritius" or answer3 == "mauritius,rwanda":
        print("Correct.")
    else:
        false_answer_count += 1
        print(f"Incorrect. You are hanging your man. your false answer count is {false_answer_count}")

    # Question 4
    # Convert the input to lowercase, then remove all spaces to attain uniformity despite user's input
    answer4 = input('Question 4: How many campuses does ALU have? Write your answer as a number:').lower().replace(" ", "")
    if answer4 == '2' or answer4 == 'two':
        print("Correct answer!")
    else:
        false_answer_count += 1
        print(f"Incorrect. You are hanging your man. your false answer count is {false_answer_count}")

    # Question 5
    # Convert the input to lowercase, then remove all spaces to attain uniformity despite user's input
    answer5 = input("Question 5: What is the name of ALU Rwanda’s Dean? (Enter the person's two names(firstname Lastname):").lower().replace(" ", "")
    if answer5 == "vedasunassee" or answer5 == 'sunasseeveda':
        print('correct answer!')
    else:
        false_answer_count += 1
        print(f"Incorrect. You are hanging your man. your false answer count is {false_answer_count}")


    # Question 6
    # Convert the input to lowercase, then remove all spaces to attain uniformity despite user's input
    answer6 = input("Question 6: Who is in charge of Student Life (Enter the person's two names(firstname Lastname):").lower().replace(" ", "")

    if answer6 == "silaogidi" or answer6 == 'ogidisila':
        print('correct answer!')
    else:
        false_answer_count += 1
        print(f"Incorrect. You are hanging your man. your false answer count is {false_answer_count}")


    game_over() #Checks if number of questions failed = 6

    # Question 7
    answer7 = input("Question 7: What is the name of our Lab?").lower()

    if answer7 == "fablab" or answer7 =='fab':
        print('correct answer!')
    else:
        false_answer_count += 1
        print(f"Incorrect. You are hanging your man. your false answer count is {false_answer_count}")

    game_over()  # Checking whether the user has already failed 6 questions

    # Question 8
    # Convert the input to lowercase, then remove all spaces to attain uniformity despite user's input
    answer8 = input("Question 8:How many students do we have in Year 2 CS?(Insert a number):").lower().replace(" ", "")
    if answer8 == "98" or answer8 == "ninetyeight" or answer8 == 'ninety-eight':
        print('correct answer!')
    else:
        false_answer_count += 1
        print(f"Incorrect. You are hanging your man. your false answer count is {false_answer_count}")

    game_over()  # Checking whether the user has already failed 6 questions

    # Question 9
    # Convert the input to lowercase, then remove all spaces to attain uniformity despite user's input
    answer9 = input("Question 9:How many degrees does ALU offer? (Insert a number):").lower().replace(" ",'')
    if answer9 == "8" or answer9 == 'eight':
        print('correct answer!')
    else:
        false_answer_count += 1
        print(f"Incorrect. You are hanging your man. your false answer count is {false_answer_count}")

    game_over()  # Checking whether the user has already failed 6 questions

    # Question 10
    answer10 = input("Question 10: Where are the headquarters of ALU?:").lower().replace(" ", "")

    if answer10 == "mauritius":
        print('correct answer!')
    else:
        false_answer_count += 1
        print(f"Incorrect. You are hanging your man. your false answer count is {false_answer_count}")


    game_over()# Checking whether the user has already failed 6 questions

    if false_answer_count == 0:#To detect if user got all questions correct
        print('Welldone. You are a true Hangman master! You got all the questions right!')
    else:
        print(f"You failed {false_answer_count} out of 10 questions. Your man survived. Not bad at all")
        false_answer_count = 0 #Resets no of false answers incase the player wants to play again

#calling the hangman game function
hangman_game()
#After the game, the following function asks the user whether they want to play again
repeat_game()
