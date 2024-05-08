"""
) Desenvolva um programa que verifique se uma frase fornecida pelo usuário é um palíndromo (ou seja, lida da mesma forma de trás para frente). Ignore espaços em branco ou sinais de pontuação, e considere maiúsculas e minúsculas da mesma forma. Seu programa deve continuar rodando até que o usuário digite "Fim".Ex:

Digite uma frase (digite "fim" para encerrar): Radar
"Radar" é palíndromo
Digite uma frase (digite "fim" para encerrar): Bom dia!
"Bom dia!" não é palíndromo
Digite uma frase (digite "fim" para encerrar): Ame o poema
"Ame o poema" é palíndromo
Digite uma frase (digite "fim" para encerrar): A Daniela ama a lei? Nada!
"A Daniela ama a lei? Nada!" é palíndromo
Digite uma frase (digite "fim" para encerrar): fim

"""

while True:
    frase = input("Digite uma frase (Digite ""fim"" para encerrar): ")
    if frase == "fim":
        break

    #para casos de maiúsula e espaços em branco
    frase_inv = frase.lower().split()
    frase_inv = "".join(frase_inv)

    if frase_inv == frase_inv[::-1]:
        print(f"{frase} é um palíndromo")
    else:
        print(f"{frase} não é um palíndromo")

    