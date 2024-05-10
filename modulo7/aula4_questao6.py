import os
import csv

with open('spotify-2023.csv', 'r', encoding='latin-1' ) as f:

    #separar as vírgulas diferenciando as que estão entre aspas
    reader = csv.reader(f)
    next(reader) #pular cabeçalho

    #lista com cada linha do arquivo
    linhas = []
    for linha in reader:
        linhas.append(linha)

    print('5 primeiras linhas: ')
    for i in range(5):
        print(linhas[i])
    print()

    print('Informações: ')

    #decidi deixar o resultado em uma lista separada
    mais_tocadas = [['','','2012','0'],['','','2013','0'],['','','2014','0'],['','','2015','0'],['','','2016','0'],['','','2017','0'],['','','2018','0'],['','','2019','0'],['','','2020','0'],['','','2021','0']]

    #percorrer todas as linhas do arquivo
    for linha in linhas:
        ano = int(linha[3])
        iterador = 0
        for i in mais_tocadas:

            #quando achar uma linha com um dos anos desejados
            if ano == int(i[2]):
                streams = int(linha[8])
                
                #verificar se o que está nos mais tocados é menor, trocando se sim
                if streams > int(i[3]):
                    mais_tocadas[iterador][0] = linha[0]
                    mais_tocadas[iterador][1] = linha[1]
                    mais_tocadas[iterador][2] = linha[3]
                    mais_tocadas[iterador][3] = linha[8]

            iterador += 1

    for i in mais_tocadas:
        print(i)