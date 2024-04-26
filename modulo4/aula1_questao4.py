n = int(input(("Escreva o número de repetições: ")))

maior = 0

while n > 0:
    x = int(input("Escreva outro número: "))

    if x > maior:
        maior = x
    else:
        n -= 1

print(maior)