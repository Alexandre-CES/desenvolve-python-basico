#pedir a temperatura em Fahrenheit
F = int(input('Graus Fahrenheit: '))

#converter para Celsius
C = (F - 32) * (5/9)

#transformar em inteiro
C = int(C)

#imprimir resultado
print(f'{F} graus Fahrenheit são {C} graus Celsius.')

