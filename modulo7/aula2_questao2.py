"""
2) Desenvolva um programa que solicite ao usuário inserir uma frase e substitua todas as ocorrências de vogal por "*".
Ex:
Digite uma frase: O rato roeu a roupa do rei
Frase modificada: * r*t* r*** * r**p* d* r**
"""

frase = input("Digite uma frase: ")
frase_modificada = ""
for i in frase:
    if i.lower() in "aeiou":
        frase_modificada += '*'
    else:
        frase_modificada += i

print(frase_modificada)