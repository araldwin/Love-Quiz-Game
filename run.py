# importing modules
"""Create a Customize Introduction
banner with color.
"""
from pyfiglet import figlet_format
from termcolor import colored

import time
"""Delaying time format."""

ascii_art = figlet_format("WELCOME\nto\nQuiz Game")
colored_ascii = colored(ascii_art, "cyan")
print(colored_ascii)

time.sleep(1)
name = input(colored("Please enter your username:\n", "green"))

while True:
    time.sleep(1)
    print()
    print(colored("Hello " + name + "!, are you ready to answer the quiz?!",
          "yellow"))
    print()
    cont = input(colored("(yes/no?):\n", "green"))
    while cont.lower() not in ("yes", "no"):
        cont = input(colored("Answer (yes/no?) only:\n", "green"))
    if cont == "yes":
        print()
        print()
        print()
        time.sleep(1)
        print()
        print(colored("loading...", "green"))
        print()
        time.sleep(2)
        print()
        print()
        print(colored("Proceeding to the first question...", "green"))
        print()
        print()
        time.sleep(1)
        break
    else:
        time.sleep(1)
        print()
        print(colored("Knowledge is Power!!!", "yellow"))
        print()
        exit()

QUESTIONS = [
    {
        "question": "In which Italian city can you find the Colosseum?",
        "options": "1. Venice\n2. Rome\n3. Naples\n4. Milan",
        "correct_option": "2",
    },
    {
        "question": "In the Big Bang Theory Tv series, "
        "what is the name of\nSheldon and Leonard’s neighbor?",
        "options": "1. Penny\n2. Patty\n3. Lily\n4. Jessie",
        "correct_option": "1",
    },
    {
        "question": "In which country was the airline Ryanair founded?",
        "options": "1. Germany\n2. Scotland\n3. Ireland\n4. Spain",
        "correct_option": "3",
    },
    {
        "question": "When was the first Harry Potter book published?",
        "options": "1. 1997\n2. 1999\n3. 2001\n4. 2003",
        "correct_option": "1",
    },
    {
        "question": "“When I find myself in times of trouble, "
        "Mother Mary comes to me”\nis the opening line of which song?",
        "options": "1. Smells like teen spirit – Nirvana\n"
        "2. Get lucky – Daft Punk\n"
        "3. Sweet Child O’ Mine – Gun N’ Roses\n4. Let it be – The Beatles",
        "correct_option": "4",
    },
    {
        "question": "Who famously said “Veni, vidi, vici”?",
        "options": "1. Winston Churchill\n2. Charles de Gaulle\n"
        "3. Julius Caesar\n4. Alexander the Great",
        "correct_option": "3",
    },
    {
        "question": "What’s Garfield favourite food?",
        "options": "1. Pizza\n2. Lasagna\n3. Burger\n4. Sandwich ",
        "correct_option": "2",
    },
    {
        "question": "How many years did Nelson Mandela spend in prison?",
        "options": "1. 7\n2. 17\n3. 27\n4. 37",
        "correct_option": "3",
    },
    {
        "question": "How high is Mount Everest?",
        "options": "1. 5,849\n2. 6,849 m\n3. 7,849 m\n4. 8,849 m",
        "correct_option": "4",
    },
    {
        "question": 'Which chemical element has "Ag" as a symbol?',
        "options": "1. Gold\n2. Silver\n3. Iron\n4. Carbon",
        "correct_option": "2",
    },
]

question_index = 0
score = 0


def display_question(questn):
    """Display question and option
    to the user.
    """
    time.sleep(1)
    print("--------------------------------------------------------------")
    print()
    print(questn["question"])
    print()
    time.sleep(2)
    print(questn["options"])
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
    if answer == correct_answer:
        global score
        score += 1
        return True
    elif answer != correct_answer:
        return False


def display_question_result(question_result, correct_answer):
    """Display message to user and
    increment the question index
    """

    if question_result:
        print("--------------------------------------------------------------")
        time.sleep(0.3)
        print(colored("Correct!", "blue"))
        time.sleep(1)
        print(colored(f"Your current score is {score}.", "yellow"))
    else:
        time.sleep(2)
        print("--------------------------------------------------------------")
        print(colored("Ooops! That was incorrect!!!", "red"))
        print("--------------------------------------------------------------")
        time.sleep(2)
        print(colored(f"The correct answer is {correct_answer}.", "blue"))
        time.sleep(2)
        print("--------------------------------------------------------------")
        print(colored(f"Your current score is {score}.", "yellow"))
    global question_index
    question_index += 1


def check_and_display_final_score():
    """If all the question is answered
    display the total score of the user
    """
    total_of_questions = len(QUESTIONS)
    if question_index == total_of_questions:
        time.sleep(2)
        print("--------------------------------------------------------------")
        print()
        print(colored("Congratulations!", "blue"))
        print()
        time.sleep(1)
        print(colored("Calculating total of scores...", "blue"))
        print()
        time.sleep(3)
        print()
        print(colored(f"Final score: {score} / {total_of_questions}",
                      "yellow"))
        print()
        print("--------------------------------------------------------------")
        print()


def play_again():
    """Display a question to the user
    if user wants to play again or end
    """
    quiz_again = input(colored("Do you want to play again? (yes or no):\n",
                       "green"))
    quiz_again = quiz_again.upper()

    if quiz_again == "YES":
        return True
    else:
        return False


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


main()

while play_again():
    main()
print()
print(colored("'Share your knowledge."
      "It is a way to achieve immortality — Dalai Lama'", "yellow"))
time.sleep(1)
print()
