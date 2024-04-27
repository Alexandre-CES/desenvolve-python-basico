import random
import math

n = int(input("Quantos valores?: "))

x = 0

for i in range(n):
    x += random.randint(0, 100)

x = math.sqrt(x)

print(x)
