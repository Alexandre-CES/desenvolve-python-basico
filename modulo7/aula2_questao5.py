"""
5) De acordo com uma pesquisa do linguista Matt Davis, o cérebro humano consegue ler palavras com as letras embaralhadas, contanto que a primeira e a última letra estejam no lugar correto. Implemente uma função chamada embaralhar_palavras() para ajudar a testar a hipótese do Matt Davis. Sua função vai receber uma frase, embaralhar as letras internas de cada palavra e retornar a frase modificada. Dica: use a biblioteca random.

Complete o seguinte código:
def embaralhar_palavras(frase):
    #### Escreva a função

# Exemplo de uso:
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)
# Possível saída: "Ptohyn é uma lignaugem de prarmoagãço"
"""

import random

def embaralhar_palavras(frase):
    frase = frase.split()
    frase_embaralhada = []
    for palavra in frase:
        #só será embaralhado se mais de 4 letras
        if len(palavra) < 4:
            frase_embaralhada.append(palavra)
            continue

        #embaralhar fatia
        fatia = list(palavra[1:-1])
        random.shuffle(fatia)

        #juntar tudo
        palavra_embaralhada = palavra[0] + ''.join(fatia) + palavra[len(palavra)-1]
        frase_embaralhada.append(palavra_embaralhada)
    
    frase_embaralhada = " ".join(frase_embaralhada)
    return frase_embaralhada

frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)



