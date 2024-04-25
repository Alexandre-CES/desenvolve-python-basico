'''
1) Escreva um programa que lê dois números e informa se a sua soma é par ou ímpar. Critério: se o resto da divisão do número por 2 for 0, o número é par, caso contrário é ímpar. Lembre-se do operador do python % que retorna o resto de uma divisão.
'''

x = int(input("Primeiro número: "))
y = int(input("Segundo número: "))

z = (x + y) % 2

print("par" if z == 0 else "impar")

