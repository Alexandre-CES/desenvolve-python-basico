import random

num_elementos = random.randint(5,20)
elementos = []
for i in range(num_elementos):
    aleatorio = random.randint(1,10)
    elementos.append(aleatorio)

print(elementos)

soma = sum(elementos)

print(soma)
print(soma / num_elementos)