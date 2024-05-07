
while True:
    cpf = input("Escreva o CPF no formato XXX.XXX.XXX-XX: ")
    if len(cpf) == 14:
        break
    else:
        print("inválido")

#obter a soma do primeiro dígito
multi = 10
soma = 0
for i in range(11):
    if cpf[i] != '.':
        soma += int(cpf[i]) * multi
        multi -= 1

#calcular primeiro dígito
d1 = soma % 11
if d1 < 2:
    d1 = 0
else:
    d1 = 11 - d1

#obter a soma do segundo dígito
multi = 11
soma = 0
for i in range(13):
    if cpf[i] != '.' and cpf[i] != '-':
        soma += int(cpf[i]) * multi
        multi -= 1

#calcular o segundo dígito
d2 = soma % 11
if d2 < 2:
    d2 = 0
else:
    d2 = 11 - d2

print(d1,d2)

if int(cpf[12]) == d1 and int(cpf[13]) == d2:
    print("válido")
else:
    print("Inválido")