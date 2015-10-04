plik = open('16.fileids', 'w')
for x in range (1,126):
    lista = "wav/file" + str(x)
    plik.write(lista)
    plik.write('\n')
plik.close()
