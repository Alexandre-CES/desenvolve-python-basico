"""
2) Escreva um script que leia o arquivo salvo no exercício anterior e salva em um novo arquivo "palavras.txt", removendo todos os espaços em branco e caracteres não alfabéticos, e separando cada palavra em uma linha. Ao final, imprima o conteúdo do arquivo "palavras.txt".
Ex:
Bom
dia
meu
nome
é
Davi
"""

import os

#coletar palavras
palavras = []
with open('frase.txt') as f:
    frase = f.read()
    palavras = frase.strip().split()

#escrever em outro arquivo separados por quebra de linha
with open('palavras.txt', 'w') as f:
    for palavra in palavras:
        f.write(palavra+'\n')