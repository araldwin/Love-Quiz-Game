# importing modules
"""
get access to code from another module by
importing the file/function using import.

 - time sleep function is used to add delay in the execution of a program.
 - sys used to manipulate different parts of the Python runtime environment.
 - pyfiglet takes ASCII text and renders it in ASCII art fonts.
 - termcolor module for Color formatting for output in the terminal.
 - make code in one module available in another.
"""
import time
import sys
from pyfiglet import figlet_format
from termcolor import colored
from data import questions


def initialize_game():
    """
    a function as the main menu of the game.
    where user name input and play game options are.
    """

    print()
    print('Welcome to:')

    ascii_art = figlet_format("Quiz Game")
    colored_ascii = colored(ascii_art, "yellow")
    print(colored_ascii)

    time.sleep(.1)

    while True:
        name = input(colored("Please enter your username:\n", "green"))
        if not name.isalnum() or len(name) > 15:
            print()
            print(colored("Invalid username!\n"
                          "Special characters are not allowed!(space)!#%&?,",
                          "red"))
            print(colored("and maximum of 15 characters only.",
                          "red"))

            print()
            print(colored("Enter alphanumeric username [A-Z, 0-9]", "green"))
            print(colored("with maximum of 15 characters only", "green"))
            continue
        break

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
    print(correct_question["question_number"])
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
    """
    conditional statement that returns
    true if the user has a correct answer from the correct option library
    and return false if its not

    as per pylint:
    R1710: Either all return statements in a function should return an expression, or none of them should.
    thats why we return None at the end of the statemnt
    """

    if answer is correct_answer:
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
    else:
        time.sleep(.1)
        print("--------------------------------------------------------------")
        print(colored("Ooops! That was incorrect!!!", "red"))
        print("--------------------------------------------------------------")
        time.sleep(.1)
        print(colored(f"The correct answer is {correct_answer}.", "blue"))


def check_and_display_final_score(player_score, total_of_questions):
    """If all the question is answered
    display the total score of the user
    """
    time.sleep(.1)
    print("--------------------------------------------------------------")
    print()
    print(colored("Congratulations!", "blue"))
    print()
    time.sleep(.1)
    print(colored("Calculating total of scores...", "green"))
    time.sleep(.1)
    print()
    print(colored(f"Final score: {player_score} / {total_of_questions}",
                  "yellow"))
    time.sleep(1.5)
    print()
    print("--------------------------------------------------------------")
    print()


def play_again():
    """
    creates variable and conditional statement
    if user wants to play again the game
    without exiting the program and run it again.
    """
    quiz_again = input(colored("Type ONLY 'YES' to play again:\n", "green"))
    quiz_again = quiz_again.upper()
    print()

    if quiz_again == "YES":
        return True
    return None


def repeat_game():
    """
    a function option whether you like to play again or not.
    """
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


def main():
    """
    Create loop for all the function above
    increment player score and question index
    using local variable and conditional statement
    """
    question_index = 0
    player_score = 0
    for question in questions:
        display_question(question)
        answer = ask_user_option()
        correct_answer = question["correct_option"]
        correct_incorrect = check_user_answer(answer, correct_answer)

        display_question_result(correct_incorrect, correct_answer)

        question_index += 1

        if correct_incorrect is True:
            player_score += 1
        time.sleep(.1)
        print("--------------------------------------------------------------")
        print(colored(f"Your current score is {player_score}.", "yellow"))

    total_of_questions = len(questions)
    if question_index == total_of_questions:
        check_and_display_final_score(player_score, total_of_questions)

    player_score = 0


if __name__ == '__main__':
    initialize_game()
    main()
    repeat_game()
