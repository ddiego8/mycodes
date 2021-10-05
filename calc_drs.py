def greeting1():
    name = input('>>>Hello there, welcome to this Calc<<< \n What is your name? \n')
    print('Hi,', name, '\n')

    greeting2()

def greeting2():
    print('Type the first number, then the second one and finally you may type the aimed function to choose it. \n')
    print('Type QUIT anytime you wish to do so - except when you are choosing the numbers >sorry xD< \n')

    insert_number()

# End/Restart machine
def again():
    ans = input('Do you want to calculate something else? Type YES or NO: \n').lower()

    if ans == 'yes':
        insert_number()

    elif ans == 'no':
        end()

    elif ans == 'quit':
        end()

    else:
        print('Perdon?') #redirect if the answer is wrong
        again()

# Quit message
def end():
    print('Okay, buh buy. Diego would like to thank you for using it. Press ENTER. \n')
    input()
    quit()

# MAIN FUNCIONS
def soma(frs, scn):
    print(frs+scn)
    again()

def minus(frs, scn):
    print(frs-scn)
    again()

def times(frs, scn):
    print(frs*scn)
    again()

def division(frs, scn):
    if frs == 0 or scn == 0:
        print('haha, funny boi ¯\_(O)_/¯')

    else:
        print(float(frs/scn))

    again()

# Start machine
def insert_number():
    try:
        fst = int(input('Insert the first number: \n'))
        scn = int(input('Insert the second number: \n'))
        func = input('Insert the function. Type SUM, MINUS, TIMES or DIVISION: \n').lower()

    except: # error mesage and restart
        print('Invalid entry, try again \n')
        insert_number()

    if func == 'sum':
        soma(fst, scn)

    elif func == 'minus':
        minus(fst, scn)

    elif func == 'times':
        times(fst, scn)

    elif func == 'division':
        division(fst, scn)

    elif func == 'quit':
        end()

    else: # error mesage and restart
        print('Invalid entry, try again \n')
        insert_number()


greeting1()
