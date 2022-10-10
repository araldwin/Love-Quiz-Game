name = input('Please enter your username: ')

while True:
    print()
    print('Hello ' + name + '!, are you ready to answer the quiz?!')
    print()
    cont = input("(yes/no?): ")
    while cont.lower() not in ("yes", "no"):
        cont = input("Answer (yes/no?) only: ")
    if cont == "yes":
        print()
        print('-----------------------------------------------------------------')
        print()
        print('awesome!...')
        print()
        print('-----------------------------------------------------------------')
        print()
        print("Proceeding to the first question...")
        print()
        break
    else:
        pass


def display_question():
    """
        1. display question to the user
        2. display options to the user
    """


def ask_user_option():
    """
    3. ask user for in put 
    4. validate user input 
    5. if user input is invalid then ask user for input again
    """


def check_user_answer():

    """
    6. if user input is valid check input with correct answer
7. if user input == correct_option of the question then increment score
"""


def display_question_result():
"""
8. display message to user 
9. increment questionIndex
"""


def check_and_display_final_score():
 # if questionIndex == size of the QUESTIONS array then display final score of the user and exit


def play_again():
# ask user to quit or play again


def main():
    """
    create loop for all the function above
    """
