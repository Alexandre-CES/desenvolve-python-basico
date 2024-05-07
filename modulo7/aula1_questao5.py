frase = input("Digite uma frase: ")
vogais = 0
i_num = 0
indices = []
for i in frase:
    if i in "aeiou":
        vogais += 1
        indices.append(i_num)
    i_num += 1

print(f"{vogais} vogais" )
print(f"índices: {indices}")