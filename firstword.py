fname = input('Enter file name: ')

tfile = open('fname', 'r')

count = 0

for line in tfile:
    if line.startswith('From:'):
        line = line.split()[1]
        print(line)
        count = count + 1

print('There were', count, 'lines in the file with From as the first word')
