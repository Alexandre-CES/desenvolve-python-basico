
#primeira lista
ql1 = int(input("Qual a quantidade de elementos da lista 1?: "))
l1 = []
for i in range(ql1):
    l1.append(int(input()))

#Segunda lista
ql2 = int(input("Qual a quantidade de elementos da lista 2?: "))
l2 = []
for i in range(ql2):
    l2.append(int(input()))

#armazenar tamanho das listas
s1 = len(l1)
s2 = len(l2)

#imprimir listas  intercaladas
print("Lista intercalada: ", end="")
for i in range(s1 + s2):
    if i < s1:
        print(l1[i], end="")
    
    if i < s2:
        print(l2[i], end="")

#saltar última linha
print("")