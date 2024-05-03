tamanho = 0

while True:
    tamanho = int(input("Qual será o tamanho da lista? (min 4): "))
    if tamanho > 3:
        break

lista = []

for i in range(tamanho):
    lista.append(int(input()))


print(lista[:]) #original
print(lista[:3]) #três primeiros
print(lista[-2:tamanho]) #dois últimos dígitos
print(lista[::-1]) #inverso

#Imagino que esteja considerando os índices e não os elementos
print(lista[::2]) #índices pares
print(lista[1::2]) #índices ímpares