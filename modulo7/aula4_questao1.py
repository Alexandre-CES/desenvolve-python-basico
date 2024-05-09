import os

frase = input("Digite uma frase: ")

#abrir arquivo e escrever frase
arquivo = open('frase.txt', 'w')
arquivo.write(frase)

#caminho do arquivo
pasta_atual = os.getcwd()
caminho = os.path.join(pasta_atual, 'frase.txt')

print(f'Frase salva em: {caminho}')
arquivo.close()

