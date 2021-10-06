# install Word method

inp = input('Enter the file name - it has be saved at the same folder: \n >')

rfile = open(inp, 'r')  

lst = list()

new = open('references_organized.txt', 'w')  #create a new file to output the references organized (currently at txt for testing)

for line in rfile:                
    line = line.rstrip()
    lst.append(line)
   
alfabetic = sorted(lista)   #blank lines still have to be treated once they have been all sorted before the references

new.writelines(alfabetic)   #write the iteration result on the new file

print('Done')
