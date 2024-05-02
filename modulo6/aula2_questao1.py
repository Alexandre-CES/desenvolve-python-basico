import random

lista = []
for i in range(20):
    aleatorio = random.randint(-100, 100)
    lista.append(aleatorio)

ordenada = sorted(lista)
maximo = max(lista)
minimo = min(lista)

print(ordenada)
print(lista)
print(maximo)
print(minimo)
