name = input('Enter your username: ')

while True:
    print('Are you ready to answer the quiz ' + name + '?')
    cont = input("(yes/no?): ")
    while cont.lower() not in ("yes", "no"):
        cont = input("please answer only (yes/no?):")
    
    if cont == "yes":
        print("Proceeding to the first question!!!")
        quit()
    else:
        continue

