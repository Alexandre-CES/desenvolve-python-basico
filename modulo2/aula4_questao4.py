'''
4) Escreva um programa que leia um valor inteiro referente a uma quantia em reais e calcule a menor quantidade possível de notas necessárias para pagar aquele valor. As notas possíveis são: 100, 50, 20, 10, 5, 2, 1. A saída deve estar formatada exatamente como indicado. 

Entrada:
576

Saída:
5 nota(s) de R$100,00
1 nota(s) de R$50,00
1 nota(s) de R$20,00
0 nota(s) de R$10,00
1 nota(s) de R$5,00
0 nota(s) de R$2,00
1 nota(s) de R$1,00
'''

#iniciando notas
nota_100, nota_50, nota_20, nota_10, nota_5, nota_2, nota_1 = 0, 0, 0, 0, 0, 0, 0

#input
dinheiro = int(input("Qual o valor?: "))

#lógica para menor quantia de notas possível
while dinheiro >= 100:
    dinheiro -= 100
    nota_100 += 1
while dinheiro >= 50:
    dinheiro -= 50
    nota_50 += 1
while dinheiro >= 20:
    dinheiro -= 20
    nota_20 += 1
while dinheiro >= 10:
    dinheiro -= 10
    nota_10 += 1
while dinheiro >= 5:
    dinheiro -= 5
    nota_5 += 1
while dinheiro >= 2:
    dinheiro -= 2
    nota_2 += 1
while dinheiro >= 1:
    dinheiro -= 1
    nota_1 += 1

#imprimir resultado
print(f'{nota_100} nota(s) de R$100,00')
print(f'{nota_50} nota(s) de R$50,00')
print(f'{nota_20} nota(s) de R$20,00')
print(f'{nota_10} nota(s) de R$10,00')
print(f'{nota_5} nota(s) de R$5,00')
print(f'{nota_2} nota(s) de R$2,00')
print(f'{nota_1} nota(s) de R$1,00')