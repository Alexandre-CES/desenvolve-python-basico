''' 
1) Faça um programa para ler as dimensões de um terreno em inteiros (comprimento e largura), bem como o preço do metro quadrado da região em ponto flutuante. Calcule o valor do terreno e imprima o resultado com a formatação apresentada a seguir.

O terreno possui 250m2 e custa R$512,490.50

Comente na linha acima de cada instrução uma breve descrição da instrução.

Fórmulas:
area_m2 = comprimento * largura
preco_total = preco_m2 * area_m2

'''

#perguntar comprimento e largura do terreno
comprimento = int(input("Comprimento: "))
largura = int(input("Largura: "))

#obter área em metro quadrado muitiplicando comprimento por largura
area_m2 = comprimento * largura

#perguntar preço por metro quadrado
preco_m2 = float(input("Preço do metro quadrado: "))

#calcular preço total baseado na multiplicação da área total pelo preço por metro quadrado
preco_total = area_m2 * preco_m2

#impressão de resultado
print(f'O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}')