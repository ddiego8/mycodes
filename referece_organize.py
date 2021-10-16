rfile = open('ADD_REF_HERE.txt', 'r')

lista = list()

new = open('references_organized.txt', 'w')

for line in rfile:        #leia cada linha verificando o sobrenome, nome do autor e guarde
    line = line.rstrip()
    lista.append(line)

alfabetico = sorted(lista)   #ordene cada linha (nome) alfabeticamente
for refline in alfabetico:
    new.writelines(refline + '\n')   #gera um novo arquivo escrevendo cada referência organizadas em uma linha e pulando para a seguinte

print('Organização concluída! =) ')
