import random

def encrypt(nomes):
    nomes_cod = []
    chave = random.randint(1,10)
    for nome in nomes:
        nome_code = ''
        for i in nome:
            tmp = ord(i)
            if tmp + chave > 126:
                i = chr(126)
            else:
                i = chr(tmp + chave)
            nome_code += i
        nomes_cod.append(nome_code)

    return nomes_cod, chave

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes, chave = encrypt(nomes)

print(nomes, chave)