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
    """
        1. display question to the user
        2. display options to the user
    """
    print(q['question'])
    print(q['options'])


def ask_user_option():
    """
       3. ask user for input 
       4. validate user input 
       5. if user input is invalid then ask user for input again
    """

    answer = input('Enter asnwer (1 - 4): ')
    return answer



# def check_user_answer():

#     """
#     6. if user input is valid check input with correct answer
#     7. if user input == correct_option of the question then increment score
#     """


# def display_question_result():

#     """
#     8. display message to user
#     9. increment questionIndex
#     """


# def check_and_display_final_score():
#  # if questionIndex == size of the QUESTIONS array then display final score of the user and exit


# def play_again():
# # ask user to quit or play again


def main():
    """
    create loop for all the function above
    """
    for question in QUESTIONS:
        display_question(question)
        asnwer = ask_user_option()


main()
