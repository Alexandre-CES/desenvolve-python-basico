"""
1) Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso. 
Dica: usando listas você não precisa fazer um "if" para cada mês.
Ex:
Digite uma data de nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973.
"""

nascimento = input("Digite sua data de nascimento(dd/mm/aaaa): ")
nascimento = nascimento.split('/')

meses = ['Janeiro','Fevereiro','Março','Abriu','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
mes = int(nascimento[1])

mes = meses[mes - 1]

print(f'Você nasceu em {nascimento[0]} de {mes} de {nascimento[2]}')