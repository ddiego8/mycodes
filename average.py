numlist = list()

while True:
    inp = input('Enten a number: ')
    if inp == 'done':
        break
    value = float(inp) #just because user can input float format and average is in float
    numlist.append(value) #register each input into the list

#it sums EACH inputed and registered number:
#len function counts whithout using count = count + 1

average = sum(numlist) / len(numlist)   #short way using functions
print('Avarage: ', average)
