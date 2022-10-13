# importing modules
"""Create a Customize Introduction
banner with color.
"""
import re
import time
import sys
from pyfiglet import figlet_format
from termcolor import colored
from data import QUESTIONS

QUESTION_INDEX = 0
SCORE = 0


ascii_art = figlet_format("Quiz Game")
colored_ascii = colored(ascii_art, "yellow")
print(colored_ascii)

time.sleep(1)


def initialize_game():

    while True:
        name = input(colored("Please enter your username:\n", "green"))
        if not re.match("^[a-z, A-Z, 0-9]*$", name):
            print()
            print(colored("Invalid username!"
                          "No special characters allowed", "red"))
        elif len(name) > 15:
            print()
            print(colored("Invalid! username too long!"
                          "Only 15 characters allowed!", "red"))
        elif name.strip() == '':
            print(colored("Invalid username!"
                          "You must enter [A-Z, 0-9]", "red"))
        else:
            break
    while True:
        time.sleep(1)
        print()
        print(colored("Hello " + name + "!, are you ready to Start the quiz?!",
                      "yellow"))
        print()
        cont = input(colored("(start/exit?):\n", "green"))
        while cont.lower() not in ("start", "exit"):
            cont = input(colored("Type (start/exit?) only:\n", "green"))
        if cont.lower() == "start":
            time.sleep(1)
            print()
            print(colored("loading...", "green"))
            time.sleep(2)
            print()
            print(colored("Proceeding to the first question...", "green"))
            print()
            time.sleep(1)
            break
        time.sleep(1)
        print()
        print(colored("Knowledge is Power!!!", "yellow"))
        print()
        print(colored("Run program again whenever you are ready!", "red"))
        sys.exit()


initialize_game()


def display_question(correct_question):
    """Display question and option
    to the user.
    """

    time.sleep(1)
    print("--------------------------------------------------------------")
    print()
    print(f"Question {QUESTION_INDEX + 1}:")
    print(correct_question["question"])
    print()
    time.sleep(2)
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
            time.sleep(2)
            print("----------------------------------------------------------"
                  "----")
            print(colored(">>>>>>>>>>INVALID INPUT<<<<<<<<<<", "red"))
            print("----------------------------------------------------------"
                  "----")
            time.sleep(1)
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
        global SCORE
        SCORE += 1
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
        time.sleep(1)
        print(colored(f"Your current score is {SCORE}.", "yellow"))
    else:
        time.sleep(2)
        print("--------------------------------------------------------------")
        print(colored("Ooops! That was incorrect!!!", "red"))
        print("--------------------------------------------------------------")
        time.sleep(2)
        print(colored(f"The correct answer is {correct_answer}.", "blue"))
        time.sleep(2)
        print("--------------------------------------------------------------")
        print(colored(f"Your current score is {SCORE}.", "yellow"))
    global QUESTION_INDEX
    QUESTION_INDEX += 1


def check_and_display_final_score():
    """If all the question is answered
    display the total score of the user
    """
    total_of_questions = len(QUESTIONS)
    if QUESTION_INDEX == total_of_questions:
        time.sleep(2)
        print("--------------------------------------------------------------")
        print()
        print(colored("Congratulations!", "blue"))
        print()
        time.sleep(1)
        print(colored("Calculating total of scores...", "green"))
        print()
        time.sleep(3)
        print()
        print(colored(f"Final score: {SCORE} / {total_of_questions}",
                      "yellow"))
        time.sleep(1.5)
        print()
        print("--------------------------------------------------------------")
        print()


def play_again():
    """Display a question to the user
    if user wants to play again or end
    """
    quiz_again = input(colored("Press 'Enter' to exit.\n"
                               "Type 'YES' to play again:\n", "green"))
    quiz_again = quiz_again.upper()

    if quiz_again == "YES":
        global SCORE
        SCORE = 0
        global QUESTION_INDEX
        QUESTION_INDEX = 0
        return True
    return None


def main():
    """
    Create loop for all the function above
    """
    for question in QUESTIONS:
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
    time.sleep(1)
    print(colored("Exiting game...", "green"))
    time.sleep(1)
    print()


if __name__ == '__main__':
    main()
    repeat_game()
