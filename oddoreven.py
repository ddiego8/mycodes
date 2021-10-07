def greeting ():
    print('>>Welcome!<< \n')
    print('>>I was created to say wheter the typed number is odd or even<< \n')

    try:
        get_number()
    except:
        print('Sorry, I could not understand :( \n')
        get_number()

def out_program():
    print('Okay, thanks for using it! See you next time.')
    input()
    quit()

def again():
    inp2 = input('Do you want to try another number? Type YES or NO. \n >').lower()
    if inp2 == 'yes':
        get_number()

    elif inp2 == 'no':
        out_program()

    else:
        print('Perdon? I did not understand')
        again()

def get_number():
    inp = int(input('Add a number and let me help you: \n >'))
    inp = inp % 2
    if inp == 0:
        print('Your number is EVEN.')
    else:
        print('Your number is ODD.')
    again()

   
greeting()
