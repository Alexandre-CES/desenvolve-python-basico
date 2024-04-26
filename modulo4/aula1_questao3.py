n1 = int(input("escreva um a nota [0/100]: "))
n2 = int(input("escreva um a nota [0/100]: "))
n3 = int(input("escreva um a nota [0/100]: "))

m = (n1 + n2 + n3) / 3

if m >= 60:
    print("Aprovado")
elif m >= 40:
    print("Recuperação")
else:
    print("Reprovado")

print("Fim")