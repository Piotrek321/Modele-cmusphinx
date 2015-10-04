plik = open('16.fileids', 'w')
for x in range (1,172):
    lista = "wav/" + str(x)
    plik.write(lista)
    plik.write('\n')
plik.close()
