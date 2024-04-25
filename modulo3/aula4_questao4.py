'''
4) Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete com base na distância e no peso do pacote. Escreva um código que solicita a distância da entrega em quilômetros e o peso do pacote em quilogramas. O programa deve calcular e imprimir o valor do frete de acordo com as seguintes regras:
Distância até 100 km: R$1 por kg.
Distância entre 101 e 300 km: R$1.50 por kg.
Distância acima de 300 km: R$2 por kg.
Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg
'''

distancia = int(input("Qual a distância em km?: "))
peso = int(input("Qual o peso em kg: "))
frete = 0

if distancia <= 100:
    frete = peso * 1
elif distancia > 100 and distancia <= 300:
    frete = peso * 1.5
else:
    frete = peso * 2

if peso > 10:
    frete += 10

print(f"O frete é de R${frete:,.2f}")