n = int(input("quantos experimentos foram realizados?: "))

S, R, C = 0, 0, 0

count = 1
while count < n + 1:
    quant = int(input(""))
    tipo = input("")

    if tipo == "S":
        S += quant
    elif tipo == "R":
        R += quant
    elif tipo == "C":
        C += quant
    else:
        print("Inválido")
    
    count += 1

total = S + R + C

print(f"Total: {total} cobaias")

print(f"Total de sapos: {S}")
print(f"Total de ratos: {R}")
print(f"Total de coelhos: {C}")

# {S + R + C = 100%} ->  {S = x%    R = y%   C = z%}  

print(f"percentual de sapos: {(S * 100) / total:.2f}%")
print(f"percentual de ratos: {(R * 100) / total:.2f}%")
print(f"percentual de coelhos: {(C * 100) / total:.2f}%")