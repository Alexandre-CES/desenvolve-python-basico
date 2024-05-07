numero = input("Digite o número: ")

if len(numero) == 8:
    print("9" + numero[0:4] + "-" + numero[4:9])
else:
    print(numero[0:5] + "-" + numero[5:9])