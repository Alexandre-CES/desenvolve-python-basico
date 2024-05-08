"""
4) Implemente uma função em Python chamada validador_senha() que verifica se uma senha fornecida atende todos os seguintes critérios:
Pelo menos 8 caracteres de comprimento.
Contém pelo menos uma letra maiúscula e uma letra minúscula.
Contém pelo menos um número.
Contém pelo menos um caractere especial (por exemplo, @, #, $).
Complete o seguinte código:
def validador_senha(senha):
    #### Escreva a função

# Exemplo de uso:
senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"
print(validador_senha(senha1))  # Saída esperada: True
print(validador_senha(senha2))  # Saída esperada: False
print(validador_senha(senha3))  # Saída esperada: False
"""

def validador_senha(senha):
    num_num, num_mai, num_min, num_esp = 0,0,0,0

    if len(senha) < 8:
        return False
    else:
        for i in senha:
            if i.isupper():
                num_mai += 1
            elif i.islower():
                num_min += 1
            elif i.isdigit():
                num_num += 1
            
            #caracteres especiais / invalidar espaços em branco
            elif not i.isdigit() and not i.isalpha() and not i == ' ':
                num_esp += 1 

        #se tiver a ocorrência de todos, retorna verdade
        if num_num > 0 and num_mai > 0 and num_min > 0 and num_esp > 0:
            return True
        else:
            return False
    

senha = input("Digite a senha: ")

print(validador_senha(senha))