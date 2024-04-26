respondentes = int(input("Quantos respondentes?: "))
media = 0

cont = respondentes # iteração
while cont > 0:
    idade = int(input("Qual sua idade?: "))
    media += idade

    cont -= 1

media /= respondentes 

print(media)