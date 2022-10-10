name = input('enter your username: ')

while True:
    print('Are you ready to answer the quiz ' + name + '?')
    cont = input("(yes/no?): ")
    while cont.lower() not in ("yes", "no"):
        cont = input("Asnwer (yes/no?) only:")   
    if cont == "yes":
        print()
        print("Proceeding to the first question!!!")
        print()
        quit()
    else:
        continue


