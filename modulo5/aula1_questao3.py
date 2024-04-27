import random

n = random.randint(1,10)

x = 0

while x != n:
    x = int(input("Adivinhe o número entre 1 e 10: "))

    if x < n:
        print("Muito baixo, tente novamente!")
    elif x > n:
        print("Muito alto, tente novamente!")

print(f"Correto! O número é {n}")