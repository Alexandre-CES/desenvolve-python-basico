import random

lista1 = []
lista2 = []
for i in range(20):
    aleatorio = random.randint(0, 50)
    lista1.append(aleatorio)
    aleatorio = random.randint(0, 50)
    lista2.append(aleatorio)

#printar as duas listas
print(f"Lista 1 - {lista1}")
print(f"Lista 2 - {lista2}")

#tranformando as listas em sets
set1 = set(lista1)
set2 = set(lista2)

#armazerar valores repetidos nos dois sets em uma nova lista
lista3 = list(set1 & set2)

#print da intersecção
print(f"intersecção {lista3}")

#contar e imprimir cada item da lista3
print("Contagem")
for i in lista3:
    c1 = lista1.count(i)
    c2 = lista2.count(i)
    print(f"{i}: (lista1 = {c1}, lista2 = {c2})")