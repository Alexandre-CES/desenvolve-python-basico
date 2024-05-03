import random

lista = []
for i in range(20):
    lista.append(random.randint(-10,10))

ma_in_com, ma_in_fim = 0,0 # começo e fim do oficial
tmp_in_com, tmp_in_fim = 0,0 #começo e fim do temporário

for i in range(len(lista)):
    if lista[i] < 0: #se encontrar negativo
        tmp_in_com = i
        for j in range(i,len(lista)): #percorra desse ponto até o final
            if lista[j] < 0: 
                tmp_in_fim = j #atualizar fim se for negativo
            else:
                break #ir ao próximo se for positivo

        #se a diferença do temporário for maior que o oficial, atualizar
        if tmp_in_fim - tmp_in_com > ma_in_fim - ma_in_com:
            ma_in_com, ma_in_fim = tmp_in_com, tmp_in_fim
       


print(lista)
print(f"Índices: {ma_in_com,ma_in_fim}")

del lista[ma_in_com:ma_in_fim + 1]

print(lista)