def contagem():
    word = input("Type a word \n >")
    count = 0
    for letter in word:
        if letter == 'a':
            count = count +1
    print(count)

def contagem2():
    word = input("Type a word \n >")
    print(word.count('a'))



contagem2()
