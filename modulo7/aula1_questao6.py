"""
Dada uma string e uma palavra objetivo, encontre todos os anagramas da palavra objetivo. Anagramas são palavras com os mesmos caracteres rearranjados.

Ex:
Digite uma frase: Meu amor mora em Roma e me deu um ramo de flores
Digite a palavra objetivo: amor
Anagramas: ["amor", "mora", "ramo", "Roma"] 
"""

#Notas para o eu de amanhã:

#teste1 = "abc"
#teste2 = "cba"
#semelhanca = 0
#tamanho = len(teste1)
#for i in teste1:
#    if i in teste2:
#        semelhanca += 1
#if semelhanca == tamanho:
#    print("sucesso")

#Faça a mesma coisa, porém com cada uma das palavras, que provavelmente terão que ser divididas de alguma forma

#Minha ideia é fazer uma lista com cada palavra e outra com os anagramas


frase = input("Digite uma frase: ")
objetivo = input("Digite uma palavra objetivo: ")
anagrama = []
#divisão das palavras
palavras = frase.split(' ')

tamanho = len(objetivo)
for palavra in palavras:
    semelhanca = 0
    for i in palavra:
        if i.lower() in objetivo.lower():
            semelhanca += 1
    if semelhanca == tamanho:
        anagrama.append(palavra)

print(anagrama)



