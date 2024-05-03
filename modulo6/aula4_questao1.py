
#criação da lista pra evitar repetição e mais linhas de código
def criarLista(com, fim, pulo=None):
    lista = []
    if pulo:
        for i in range(com, fim + 1, pulo):
            lista.append(i)
    else:
        for i in range(com, fim + 1):
            lista.append(i)
    return lista

#pares
lista = criarLista(20, 50)
pares = [i for i in lista if (i % 2) == 0]
print(pares)

#quadrados
lista = criarLista(1, 9)
quadrados = [i**2 for i in lista]
print(quadrados)

#divisível por 7
lista = criarLista(1,100)
divi7 = [i for i in lista if (i%7) == 0]
print(divi7)

#paridade
lista = criarLista(0,30, 3)
paridade = ['par' if (i % 2) == 0 else 'ímpar' for i in lista]
print(paridade)