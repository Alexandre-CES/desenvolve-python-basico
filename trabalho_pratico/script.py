import csv
import os

logs = open('logs.txt','w')

#criar arquivos necessários se não existirem
def create_files():
    path = os.getcwd()
    
    if not os.path.exists(f'{path}/products.csv'):
        with open('products.csv','w') as file:
            file.write('id,name,price,amount')
    
    if not os.path.exists(f'{path}/users.csv'):
        with open('users.csv','w') as file:
            file.write('id,user,password,permition\n0,owner,00000,3')
    
#função para lógica de login
def Login():

    isLogged = False

    #pegar a lista de todos os usuários cadastrados
    users = []
    with open('users.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            users.append(row)

    while not isLogged:
        user_input = input('User: ')
        password_input = input('Password: ')

        #checar se usuário e senha estão corretos
        for i in range(len(users)):
            if users[i]['user'] == user_input and users[i]['password'] == password_input:
                isLogged = True
                logs.write(f'user {users[i]["id"]} logged\n')
                Main(users[i]['id'], user_input, int(users[i]['permition']))
                break
           
            #se apos checar tudo não achar
            if i >= len(users) - 1 and not isLogged:
                print('credenciais inválidas')
                break
        
        #para sair se não lembrar da conta
        if not isLogged:
            option = input('Quer sair? [s/n]: ')
            if option.lower().strip() == 's':
                program_exit()
        
#onde o usuário escolherá o que fazer
def Main(id, user, permition):
    print(f'Bem-vindo(a) {user}!')

    #só vai sair quando o usuário pedir
    while True:
        print('O que você gostaria de fazer?');print('')
        print('[0]sair - [1]trocar usuário - [2]caixa',end=' ')

        #permissões para pessoas com cargo maior
        if permition > 1:
            print(' - [3]Gerenciar produtos', end='')

        print('')

        #para não crashar se escrever algo que não for um número
        while True:
            option = input('')
            if option.isdigit():
                option = int(option)
                break
            else:
                print('Opção inválida')

        if option == 0:
            program_exit()
        elif option == 1:
            Login()
            break
        elif option == 2:
            cashier(id, user)
            break
        elif permition > 1 and option == 3:
            management(id, user)
        else:
            print('Opção inválida')

#onde dados dos produtos podem ser alterados
def management(id, user):
    logs.write('went to management function\n')

    while True:
        
        print('O que deseja fazer?')
        print('[1]Criar - [2]Atualizar - [3]Deletar')

        while True:
            option = input('')
            if option.isdigit():
                option = int(option)
                break
            else:
                print('Opção inválida')
        
        #adicionar produto
        if option == 1:
            
            print('insira os dados do produto')
            while True:
                product_id = input('ID: ')
                products = create_product_list()
                if product_id not in (i['id'] for i in products):
                    break
                else:
                    print('id já está sendo usado')
                    
            product_name = input('Nome: ')
            product_price = input('Preço unitário: ')
            product_amount = input('Quantidade: ')

            with open('products.csv','a') as file:
                file.write('\n')
                file.write(f'{product_id},{product_name},{product_price},{product_amount}')

        #modificar produto
        elif option == 2:
            while True:
                product_id = input('ID: ')
                products = create_product_list()
                if product_id not in (i['id'] for i in products):
                    print('id não encontrado')
                    option = input('Quer Voltar ao Menu principal?[s/n]: ')
                    if option.lower().strip() == 's':
                        break
                else:
                    print('O que deseja modificar?')
                    print('[1]Nome - [2]Preço unitário - [3]Quantidade - [4]Todos')
                    while True:
                        option = input('')
                        if option.isdigit():
                            option = int(option)
                            if option < 1 or option > 4:
                                ('Opção inválida')
                                continue   
                            break
                        else:
                            print('Opção inválida')

                    new_name,new_price,new_amount = False,False,False
                    if option == 1 or option == 4:
                        new_name = input('Novo nome: ')
                    if option == 2 or option == 4:
                        new_price = input('Novo preço: ')
                    if option == 3 or option == 4:
                        new_amount = input('Nova quantidade')

                    update_products(new_name,new_price,new_amount)

                    option = input('Quer alterar outro produto?[s/n]: ')
                    if option.lower().strip() == 'n':
                        break
                    

        option = input('Quer continuar gerenciando?[s/n]: ')
        if option.lower().strip() == 'n':
            break

#onde será feita a venda de produtos
def cashier(id, user):
    logs.write('went to cashier function\n')
    products = create_product_list()
    print('caixa')
   
#criar uma lista com os produtos disponíveis e suas informações
def create_product_list():
    products = []
    with open('products.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append(row)
    logs.write('Products list created\n')
    return products


'''função para atualizar dados
Todos estão com falso como padrão, assim só será modificado os valores que forem passados'''
def update_products(new_name=False,new_price=False,new_amount=False):
    print(new_name,new_price,new_amount)

#função para sair do programa de forma segura
def program_exit():
    logs.write('program exit')
    logs.close()
    quit()

if __name__ == '__main__':
    create_files()
    Login()
    program_exit()