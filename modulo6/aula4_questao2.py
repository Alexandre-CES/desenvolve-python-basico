lista_vogais = ['a','e','i','o','u']
lista_consoantes = ['b','c', 'd', 'f', 'g', 'h' ,'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

frase = input("Digite uma frase: ")

vogais = [i for i in frase if (i.lower() in lista_vogais)]
consoantes = [i for i in frase if (i.lower() in lista_consoantes)]

print(f'vogais: {vogais}')
print(f'consoantes: {consoantes}')