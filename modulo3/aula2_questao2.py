'''
2) Dando continuidade à questão anterior, um outro bar permite a entrada de grupos onde pelo menos uma pessoa é maior de idade (ficando responsável pelas outras). Ajuste sua resposta da questão anterior, ainda solicitando as idades de Juliana e Cris, mas ajustando a expressão para esse novo cenário, imprimindo True se puderem entrar no bar, e False caso contrário.
'''

idade_Juliana = int(input("Idade de Juliana: "))
idade_Cris = int(input("Idade de Cris: "))

print(idade_Juliana  > 17 or idade_Cris > 17)

