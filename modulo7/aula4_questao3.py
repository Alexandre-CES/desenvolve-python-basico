"""
O texto das primeiras 25 linhas
O número de linhas do arquivo
A linha com maior número de caracteres
O número de menções aos nomes dos personagens "Nonato" e "Íria" (inclua todas as variações de maiúsculas e minúsculas e atenção para não incluir a substring "iria" se ela fizer parte de outras palavras).
"""

import os

with open('estomago.txt') as f:
    roteiro = f.read()

    linhas = roteiro.split('\n')
    
    #print das primeiras 25 linhas 
    for i in range(25):
        print(linhas[i])
    print()

    #linhas do arquivo
    print(f'Linhas: {len(linhas)}')
    print()

    #maior linha
    print(f'A maior linha é: {max(linhas, key=len)}')
    print()

    #menções de "Nonato" e "Íria"
    palavras = roteiro.split()
    mencoes = 0
    for palavra in palavras:
        #Imagino que, por estar verificando por cada palavra separadamente, não irá incluir substrings
        if palavra == "Nonato" or palavra == "Íria":
            mencoes += 1
    print(f'Número de menções de "Nonato" e "Íria": {mencoes}')