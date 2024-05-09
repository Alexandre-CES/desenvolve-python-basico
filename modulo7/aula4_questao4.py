'''
Escreva um programa em Python para executar o jogo, de acordo com as definições:
Abra o arquivo "gabarito_forca.txt" e escolha aleatoriamente uma palavra;
Com o arquivo "gabarito_enforcado.txt", crie uma lista de strings com os estágios do enforcado;
No início exiba o número de letras da palavra sorteada como underscores;
Permita que o jogador insira letras para adivinhar a palavra;
Em caso de acerto, mostre o progresso do jogador substituindo os underscores correspondentes à letra digitada;
Em caso de erro, crie a função "imprime_enforcado()" que recebe um inteiro indicando o número de erros do jogador e imprime o enforcado correspondente;
Limite o número de tentativas para 6 (as partes do enforcado).
'''

import os
from sys import exit
import random


def Main():
    #escolha da palavra aleatória
    palavra = ''
    with open('gabarito_forca.txt') as f:
        palavras = f.read().split('\n')
        escolha = random.randint(0,9)
        palavra = palavras[escolha]
        print(palavra)

    #criar lista com cada parte da forca
    forca = []
    with open('gabarito_enforcado.txt') as f:
        linhas = f.read().split('\n')

        com = 0
        fim = 5

        #dividir as partes
        for i in range(7):
            linha_atual = '\n'.join(linhas[com:fim])
            forca.append(linha_atual)
            com += 6
            fim += 6
    print(forca[0])

    #Nota para corretor: "Por algum motivo os underscores estão invisíveis para mim, então fiz com esse outro, espero que não seja um problema"

    #criar barra de progresso com scores
    progresso = ['-'] * len(palavra)

    erros = 0
    #repitir enquanto não souber a palavra
    while '-' in progresso:
        #adivinhar uma única letra
        letra = ''
        while True:
            letra = input('Adivinhe uma letra: ')
            if len(letra) == 1 and letra.isalpha():
                break
            print("Tem que ser uma letra")

        #se for repetida
        if letra in progresso:
            print("essa já foi")
            continue
        
        #se a letra for certa
        if letra in palavra:
            print('acertou!')

            #atualizará todos os espaços com essa letra
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    progresso[i] = letra
                print(progresso[i], end="")
            print()
        else:
            erros += 1
            imprime_enforcado(forca, erros)

    #quando sair do loop (todos os espaços em branco preenchidos)
    print(f'Parabéns! A palavra era {palavra}')

def imprime_enforcado(forca, erros):
    print(forca[erros])
    if erros >= 6:
        print('Você perdeu')
        exit()

Main()