# importing modules
"""
get access to code from another module by
importing the file/function using import.

 - time sleep function is used to add delay in the execution of a program.
 - sys used to manipulate different parts of the Python runtime environment.
 - pyfiglet takes ASCII text and renders it in ASCII art fonts.
 - termcolor module for Color formatting for output in the terminal.
 -  make code in one module available in another.
"""
import time
import sys
from pyfiglet import figlet_format
from termcolor import colored
from data import questions

QUESTION_INDEX = 0
PLAYER_SCORE = 0


def initialize_game():

    print()
    print('Welcome to:')

    ascii_art = figlet_format("Quiz Game")
    colored_ascii = colored(ascii_art, "yellow")
    print(colored_ascii)

    time.sleep(.1)

    while True:
        name = input(colored("Please enter your username:\n", "green"))
        if name.isalnum():
            break

        if len(name) > 15:
            print()
            print(colored("Username too long! "
                          "Only 15 characters allowed!", "red"))

        print()
        print(colored("Invalid username!\n"
                      "Special characters are not allowed!(space)!#%&?.",
                      "red"))
        print()
        print(colored("Enter alphanumeric username [A-Z, 0-9]", "green"))

    while True:
        time.sleep(.1)
        print()
        print(colored("Hello " + name + "!, are you ready to Start the quiz?!",
                      "yellow"))
        print()
        cont = input(colored("(start/exit?):\n", "green"))
        while cont.lower() not in ("start", "exit"):
            cont = input(colored("Type (start/exit?) only:\n", "green"))
        if cont.lower() == "start":
            time.sleep(.1)
            print()
            print(colored("loading...", "green"))
            time.sleep(.1)
            print()
            print(colored("Proceeding to the first question...", "green"))
            print()
            time.sleep(.1)
            break
        time.sleep(.1)
        print()
        print(colored("Knowledge is Power!!!", "yellow"))
        print()
        print(colored("Run program again whenever you are ready!", "red"))
        sys.exit()


def display_question(correct_question):
    """Display question and option
    to the user.
    """

    time.sleep(.1)
    print("--------------------------------------------------------------")
    print()
    print(f"Question {QUESTION_INDEX + 1}:")
    print(correct_question["question"])
    print()
    time.sleep(.1)
    print(correct_question["options"])
    print()


def ask_user_option():
    """Asked for user input and validate, if user input
    is invalid ask for user input again
    """
    while True:
        time.sleep(.5)
        answer = input(colored("Enter answer (1 - 4):\n", "green"))
        print()
        if answer not in ("1", "2", "3", "4"):
            time.sleep(.1)
            print("----------------------------------------------------------"
                  "----")
            print(colored(">>>>>>>>>>INVALID INPUT<<<<<<<<<<", "red"))
            print("----------------------------------------------------------"
                  "----")
            time.sleep(.1)
            print()
            print(colored("Choose your answer (1, 2, 3, or 4)?", "green"))
            print()
        else:
            break
    return answer


def check_user_answer(answer, correct_answer):
    """Incrementing user score only if it
    is correct answer
    """
    if answer is correct_answer:
        global PLAYER_SCORE
        PLAYER_SCORE += 1
        return True
    if answer != correct_answer:
        return False
    return None


def display_question_result(question_result, correct_answer):
    """Display message to user and
    increment the question index
    """

    if question_result:
        print("--------------------------------------------------------------")
        time.sleep(0.3)
        print(colored("Correct!", "blue"))
        time.sleep(.1)
        print(colored(f"Your current score is {PLAYER_SCORE}.", "yellow"))
    else:
        time.sleep(.1)
        print("--------------------------------------------------------------")
        print(colored("Ooops! That was incorrect!!!", "red"))
        print("--------------------------------------------------------------")
        time.sleep(.1)
        print(colored(f"The correct answer is {correct_answer}.", "blue"))
        time.sleep(.1)
        print("--------------------------------------------------------------")
        print(colored(f"Your current score is {PLAYER_SCORE}.", "yellow"))
    global QUESTION_INDEX
    QUESTION_INDEX += 1


def check_and_display_final_score():
    """If all the question is answered
    display the total score of the user
    """
    total_of_questions = len(questions)
    if QUESTION_INDEX == total_of_questions:
        time.sleep(.1)
        print("--------------------------------------------------------------")
        print()
        print(colored("Congratulations!", "blue"))
        print()
        time.sleep(.1)
        print(colored("Calculating total of scores...", "green"))
        print()
        time.sleep(.1)
        print()
        print(colored(f"Final score: {PLAYER_SCORE} / {total_of_questions}",
                      "yellow"))
        time.sleep(1.5)
        print()
        print("--------------------------------------------------------------")
        print()


def play_again():
    """Display a question to the user
    if user wants to play again or end
    """
    quiz_again = input(colored("Type ONLY 'YES' to play again:\n", "green"))
    quiz_again = quiz_again.upper()

    if quiz_again == "YES":
        global PLAYER_SCORE
        PLAYER_SCORE = 0
        global QUESTION_INDEX
        QUESTION_INDEX = 0
        return True
    return None


def main():
    """
    Create loop for all the function above
    """
    for question in questions:
        display_question(question)
        answer = ask_user_option()
        correct_answer = question["correct_option"]
        correct_incorrect = check_user_answer(answer, correct_answer)
        display_question_result(correct_incorrect, correct_answer)
        check_and_display_final_score()


def repeat_game():
    while play_again():
        main()
    print()
    print(colored("'Share your knowledge. "
                  "It is a way to achieve immortality"
                  " — Dalai Lama'", "yellow"))
    time.sleep(.1)
    print(colored("Exiting game...", "green"))
    time.sleep(.1)
    print()


if __name__ == '__main__':
    initialize_game()
    main()
    repeat_game()
