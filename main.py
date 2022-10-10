#importing modules
from pyfiglet import figlet_format
from termcolor import colored

import time

ascii_art = figlet_format('WELCOME')
colored_ascii = colored(ascii_art, 'green')
print(colored_ascii)

time.sleep(1)
name = input('Please enter your username: ')

while True:
    time.sleep(1)
    print()
    print('Hello ' + name + '!, are you ready to answer the quiz?!')
    print()
    cont = input("(yes/no?): ")
    while cont.lower() not in ("yes", "no"):
        cont = input("Answer (yes/no?) only: ")
    if cont == "yes":
        print()
        print('-----------------------------------------------------------------')
        time.sleep(1)
        print()
        print('awesome!...')
        print()
        time.sleep(2)
        print('-----------------------------------------------------------------')
        print()
        print("Proceeding to the first question...")
        print()
        time.sleep(2)
        break
    else:
        pass
    time.sleep(1)
    
QUESTIONS = [{
    'question': 'In which Italian city can you find the Colosseum?',
    'options': '1. Venice\n2. Rome\n3. Naples\n4. Milan',
    'correct_option': '2'
},
    {
    'question': 'In the Big Bang Theory Tv series, what is the name of Sheldon and Leonard’s neighbor?',
    'options': '1. Penny\n2. Patty\n3. Lily\n4. Jessie',
    'correct_option': '1'
},
    {
    'question': 'In which country was the airline Ryanair founded?',
    'options': '1. Germany\n2. Scotland\n3. Ireland\n4. Spain',
    'correct_option': '3'
},
    {
    'question': 'When was the first Harry Potter book published?',
    'options': '1. 1997\n2. 1999\n3. 2001\n4. 2003',
    'correct_option': '1'
},
    {
    'question': '“When I find myself in times of trouble, Mother Mary comes to me” is the opening line of which song?',
    'options': '1. Smells like teen spirit – Nirvana\n2. Get lucky – Daft Punk\n'
               '3. Sweet Child O’ Mine – Gun N’ Roses\n4. Let it be – The Beatles',
    'correct_option': '4'
},
    {
    'question': 'Who famously said “Veni, vidi, vici”?',
    'options': '1. Winston Churchill\n2. Charles de Gaulle\n3. Julius Caesar\n4. Alexander the Great',
    'correct_option': '3'
},
    {
    'question': 'What’s Garfield favourite food?',
    'options': '1. Pizza\n2. Lasagna\n3. Burger\n4. Sandwich ',
    'correct_option': '2'
},
    {
    'question': 'How many years did Nelson Mandela spend in prison?',
    'options': '1. 7\n2. 17\n3. 27\n4. 37',
    'correct_option': '3'
},
    {
    'question': 'How high is Mount Everest?',
    'options': '1. 5,849\n2. 6,849 m\n3. 7,849 m\n4. 8,849 m',
    'correct_option': '4'

},
    {
    'question': 'Which chemical element has "Ag" as a symbol?',
    'options': '1. Gold\n2. Silver\n3. Iron\n4. Carbon',
    'correct_option': '2'
}]

questionIndex = 0
score = 0


def display_question(q):
    """display question and option
       to the user.
    """
    time.sleep(1)
    print('-----------------------------------------------------------------')
    print()
    print(q['question'])
    print()
    time.sleep(2)
    print(q['options'])
    print()


def ask_user_option():
    """asked for user input and validate, if user input
       is invalid ask for user input again
    """
    while True:
        time.sleep(1)
        answer = input('Enter answer (1 - 4): ')
        print()
        if answer not in ('1', '2', '3', '4'):
            time.sleep(2)
            print('----------------------------------------------------------')
            print('INVALID INPUT')
            print('----------------------------------------------------------')
            time.sleep(1)
            print()
            print('Choose your answer (1, 2, 3, or 4)?')
            print()
        else:
            break
    return answer


def check_user_answer(answer, correct_answer):
    """incrementing user score only if it
       is correct answer
    """
    if answer == correct_answer:
        global score
        score += 1
        return True
    elif answer != correct_answer:
        return False

def display_question_result(question_result, correct_answer):
    """display message to user and
       increment the question index
    """

    if question_result:
        print('-------------------------------------------------------------')
        time.sleep(.5)
        print('Correct!')
        time.sleep(1)
        print(f'Your current score is {score}.')
    else:
        time.sleep(2)
        print('--------------------------------------------------------------')
        print('Ooops! That was incorrect!!!')
        print('--------------------------------------------------------------')
        time.sleep(2)
        print(f'The correct answer is {correct_answer}.')
        time.sleep(2)
        print('--------------------------------------------------------------')
        print(f'Your current score is {score}.')
    global questionIndex
    questionIndex += 1


def check_and_display_final_score():
    """if all the question is answered
       display the total score of the user
    """
    total_of_questions = len(QUESTIONS)
    if questionIndex == total_of_questions:
        time.sleep(2)
        print('--------------------------------------------------------------')
        print()
        print(f'Final score: {score} / {total_of_questions}')
        print()
        print('--------------------------------------------------------------')
        print()


def play_again():
    """display a question to the user
       if user wants to play again or end
    """
    quiz_again = input("Do you want to play again? (yes or no): ")
    quiz_again = quiz_again.upper()

    if quiz_again == "YES":
        return True
    else:
        return False

def main():
    """
    create loop for all the function above
    """
    for question in QUESTIONS:
        display_question(question)
        answer = ask_user_option()
        correct_answer = question['correct_option']
        correct_incorrect = check_user_answer(answer, correct_answer)
        display_question_result(correct_incorrect, correct_answer)
        check_and_display_final_score()

main()

while play_again():
    main()
print("'Share your knowledge. It is a way to achieve immortality — Dalai Lama'")