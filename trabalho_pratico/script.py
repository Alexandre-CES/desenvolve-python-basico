import csv
import os

#Muitas opções tratam qualquer coisa que não for "n" como sim, preferi fazer assim para agilizar, assim você pode só apertar enter para confirmar, só não fiz assim na de deletar, por motivos de segurança

logs = open('logs.txt','w')

def create_files():
    '''criar arquivos necessários se não existirem'''

    #automaticamente criará o usuário owner, que pode gerar produtos e outros usuários
    path = os.getcwd()
    if not os.path.exists(f'{path}/products.csv'):
        with open('products.csv','w') as file:
            file.write('id,name,price,amount')
    if not os.path.exists(f'{path}/users.csv'):
        with open('users.csv','w') as file:
            file.write('id,user,password,permission\n0,owner,00000,3')
    
def Login():
    '''função para lógica de login'''

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
                Main(users[i]['id'], user_input, int(users[i]['permission']))
                break
           
            if i >= len(users) - 1 and not isLogged:
                print('credenciais inválidas')
                break
        
        #Opção de sair
        if not isLogged:
            option = input('Quer sair? [s/n]: ')
            if option.lower().strip() == 's':
                program_exit()
        
def Main(id, user, permission):
    '''onde o usuário escolherá o que fazer'''

    print('-------------------------');print('')
    print(f'Bem-vindo(a) {user}!');print('')

    #só vai sair quando o usuário pedir
    while True:
        maximum = 2
        print('O que você gostaria de fazer?');print('')
        print('[0]sair - [1]trocar usuário - [2]Lista de produtos',end=' ')

        #permissões para pessoas com cargo maior
        if permission >= 1:
            maximum = 3
            print(' - [3]Caixa', end='')
        if permission >= 2:
            maximum = 4
            print(' - [4]Gerenciar', end='')

        print('')

        option = while_option(0,maximum);print('')

        if option == 0:
            program_exit()
        elif option == 1:
            logs.write(f'user {id} left\n')
            Login()

        elif option == 2:
            print('gerando lista de produtos:')
            print('-----------------------')
            products = read_product_list()
            for product in products:
                print(f'{product["name"]} / R${product["price"]}')
            input('.')

        elif permission >= 1 and option == 3:
            cashier(id, user)
        elif permission >= 2 and option == 4:
            management(id, user, permission)
        else:
            print('Opção inválida');print('')

#Gerenciar----------------------------------------------------

def management(id, user, permission):
    '''onde dados dos produtos podem ser alterados'''

    logs.write('went to management function\n')

    while True:
        print('--------------------------------')
        print(f'O que deseja gerenciar {user}?');print('')
        print('[0]Voltar - [1]Gerenciar produtos - [2]Gerenciar usuários')

        option = while_option(0,3);print('')
        
        if option == 0:
            break
        #gerenciar produtos
        elif option == 1:
            while True:
                print('----------------------------------')
                print('Qual modificação fará em produtos?');print('')
                print('[0]Voltar - [1]Criar produto - [2]Modificar produto - [3]Deletar produto')

                option = while_option(0,3);print('')

                if option == 0:
                    break
                #adicionar produto
                elif option == 1:
                    print('Criando produto:')
                    create_products()
                #modificar produto
                elif option == 2:
                    print('Modificando produto: ')
                    while True:
                        product_id = input('Digite o ID do produto: ');print('')
                        if verify_product_id(product_id):
                            print('O que deseja modificar?');print('')
                            print('[0]Voltar - [1]Nome - [2]Preço unitário - [3]Quantidade - [4]Todos');print('')

                            update_product_manager(product_id)

                        option = input('Quer alterar outro produto?[s/n]: ');print('')
                        if option.lower().strip() == 'n':
                            break

                #deletar produto
                elif option == 3:
                    while True:
                        print('Deletando produto: ')
                        product_id = input('Digite o ID do produto que deseja deletar: ')
                        if verify_product_id(product_id):
                            option = input('Tem certeza?[s/n]: ')
                            if option.lower().strip() == 's':
                                delete_product(product_id)    
                            else:
                                print('operação cancelada')

                        option = input('Quer deletar outro produto?[s/n]: ');print('')
                        if option.lower().strip() == 'n':
                            break
        #Gerenciar usuários
        elif option == 2:
            while True:
                print('---------------------------------')
                print('Que modificação fará em usuários?');print('')
                print('[0]Voltar - [1]Adicionar usuários - [2]Modificar dados de usuário - [3]Deletar usuário')

                option = while_option(0,3);print('')

                if option == 0:
                    break
                elif option == 1:
                    print('Adicionando usuário: ')
                    create_users()
                elif option == 2:
                    print('Modificando usuário: ')
                    while True:
                        user_id = input('Digite o ID do usuário: ');print('')
                        if verify_user_id(user_id):

                            ind, users = get_users_index(user_id)

                            if permission < int(users[ind]['permission']):
                                print('Você não tem permissão para isso')
                            
                            else:
                                print(f'O que deseja modificar do usuário {users[ind]["user"]}?');print('')
                                print('[0]Voltar - [1]Usuário - [2]Senha - [3]Permissão - [4]Todos');print('')
                            
                                update_user_manager(user_id)

                        option = input('Quer alterar outro usuário?[s/n]: ');print('')
                        if option.lower().strip() == 'n':
                            break

                elif option == 3:     
                    while True:
                        print('Deletando usuário: ')
                        user_id = input('Digite o ID do usuário que deseja deletar: ')
                        if verify_product_id(user_id):
                            option = input('Tem certeza?[s/n]: ')
                            if option.lower().strip() == 's':
                                delete_user(user_id)    
                            else:
                                print('operação cancelada')

                        option = input('Quer deletar outro usuário?[s/n]: ');print('')
                        if option.lower().strip() == 'n':
                            break

def update_user_manager(user_id,new_user=False,new_password=False,new_permission=False):
    '''função para modificar dados de usuários na lista. 
    Todos estão com falso como padrão, assim só será modificado os valores que forem passados'''

    #escolher o que quer trocar
    option = while_option(0,4)
    if option == 0:
        return
    if option == 1 or option == 4:
        new_user = input('Novo usuário: ')
    if option == 2 or option == 4:
        new_password = input('Nova senha: ')
    if option == 3 or option == 4:
        new_permission = input('Novo nível de permissão: ')

    ind, users = get_users_index(user_id)
    
    #renomear na lista
    if new_user:
        users[ind]['user'] = new_user
    if new_password:
        users[ind]['password'] = new_password
    if new_permission:
        users[ind]['permission'] = new_permission

    update_users(users);print('')

def update_product_manager(product_id,new_name=False,new_price=False,new_amount=False):
    '''função para modificar dados de produtos na lista. 
    Todos estão com falso como padrão, assim só será modificado os valores que forem passados'''

    option = while_option(0,4)
    if option == 0:
        return
    if option == 1 or option == 4:
        new_name = input('Novo nome: ')
    if option == 2 or option == 4:
        new_price = input('Novo preço: ')
    if option == 3 or option == 4:
        new_amount = input('Nova quantidade: ')

    ind, products = get_product_index(product_id)
    
    #renomear na lista
    if new_name:
        products[ind]['name'] = new_name
    if new_price:
        products[ind]['price'] = new_price
    if new_amount:
        products[ind]['amount'] = new_amount

    update_products(products)

#caixa----------------------------------------------------------------------

def cashier(id, user):
    '''onde será feita a venda de produtos'''

    logs.write('went to cashier function\n')
    print('---caixa iniciado---')

    while True:
        print('O que deseja fazer?');print('')
        print('[0]Voltar - [1]Realizar venda');print('')

        option = while_option(0,1)
        
        if option == 0:
            return
        elif option == 1:

            #cada venda inicia um looping
            while True:
                print('---------------------------------------')
                logs.write(f'\n({id}){user} started a sale\n')
                current_sell_product_list = [] #lista de compras
                total = 0
                
                #loop até os dados estarem corretos ou o usuário decidir cancelar
                while True:
                    product_repeated = False
                    print('')
                    product_id = input('ID do produto: ')
                    
                    #se digitar um produto que já está na lista, pode mudar sua quantidade ou tirá-lo
                    ind = 0
                    for item in current_sell_product_list:
                        if item['id'] == product_id:
                            print('produto já está na lista')
                            product_repeated = True
                            option = input('quer mudar a quantidade?[s/n]: ')
                            if option.lower().strip() != 'n':
                                ind, products = get_product_index(product_id)
                                product_amount = products[ind]['amount']
                                
                                print(f'Digite a nova quantidade: ', end='')
                                new_amount = while_option(0)
                                
                                if new_amount > int(product_amount):
                                    print('Quantidade excede o estoque disponível')
                                else:
                                    item['amount'] = new_amount
                                    item['sell_price'] = new_amount * float(products[ind]['price'])
                                    logs.write('Product amount updated\n')
                                break
                            else:
                                option = input('quer removê-lo da lista?: ')
                                if option.lower().strip() == 's': #deixei esse como sim para evitar apagar sem querer
                                    logs.write(f'product {item["id"]} removed from list')
                                    del(current_sell_product_list[ind])

                                break
                        ind += 1  

                    #só adicionará na lista se ele não estiver nela
                    if not product_repeated:
                        if verify_product_id(product_id):
                            print('Qual a quantidade?: ', end='')
                            sell_amount = while_option(0)
                            
                            ind, products = get_product_index(product_id)
                            
                            #ter certeza de existir a quantidade a ser vendida
                            product_amount = products[ind]['amount']
                            if sell_amount > int(product_amount):
                                print('Está tentando vender mais do que há no estoque')
                                continue

                            product_price = products[ind]['price']

                            #preço total do produto atual
                            sell_price = sell_amount * float(product_price)
                            
                            #adicionar dados da compra do produto na lista
                            current_sell_product_list.append({
                                'id':product_id,
                                'name':products[ind]['name'],
                                'amount':sell_amount,
                                'sell_price':sell_price
                            })

                            total += sell_price

                            logs.write('New product added to the list\n')
                    
                    #ver se quer adicionar mais coisas antes de concluir venda
                    option = input('Quer digitar outro ID?[s/n]: ')
                    if option.lower().strip() == 'n':
                        option = input('Concluir venda?: ')
                        if option.lower().strip() == 'n': # o mesmo aqui
                            print('Operação cancelada')
                            logs.write('Operation canceled\n')
                        else:
                            update_amount_cashier(current_sell_product_list)
                        break
                
                logs.write(f'Products sold by ({id}){user}! Total: {total}\n\n') 

                #caso a pessoas for sair
                option = input('Quer realizar outra venda?[s/n]: ')
                if option.lower().strip() == 'n':
                    break
        else:
            print('Opção inválida')

def update_amount_cashier(product_list):
    '''Para dar update na quantidade dos produtos vendidos no caixa. Decidi deixar separado para que o código fique mais claro'''
    
    products = read_product_list()
    for item in product_list:
        product_id = item['id']

        ind = get_product_index(product_id, False)
        
        products[ind]['amount'] = int(products[ind]['amount']) - int(item['amount'])

    update_products(products)

#CRUD------------------------------------------------------------------------------------------

def create_users():
    print('Insira os dados do usuário')
    #verifica se id desejado já está em uso
    while True:
        user_id = input('ID: ')
        if user_id.strip() == '':
            continue
        users = read_user_list()
        if user_id not in (i['id'] for i in users):
            break
        else:
            print('id já está sendo usado')
    
    while True:
        user_user = input('Usuário: ')
        user_password = input('Senha: ')

        if user_user != '' and user_password != '':
            break
        else:
            print('Dados inválidos')

    print('Nível de permissão: ', end='')
    user_permission = while_option(0,3)

    #adicionar usuário no arquivo
    with open('users.csv','a') as file:
        file.write('\n')
        file.write(f'{user_id},{user_user},{user_password},{user_permission}')

    logs.write(f'created user {user_user} id:{user_id}\n')

def create_products():
    '''Função para criar produtos'''

    print('insira os dados do produto')

    #verifica se id desejado já está em uso
    while True:
        product_id = input('ID: ')
        if product_id.strip() == '':
            continue
        products = read_product_list()
        if product_id not in (i['id'] for i in products):
            break
        else:
            print('id já está sendo usado')
        
    while True:
        product_name = input('Nome: ')
        if product_name.strip() != '':
            break

    print('Preço unitário: ')
    product_price = while_option(0,False,True)

    print('Quantidade: ', end='')
    product_amount = while_option(0)

    #adicionar produto no arquivo
    with open('products.csv','a') as file:
        file.write('\n')
        file.write(f'{product_id},{product_name},{product_price},{product_amount}')

    logs.write(f'created product {product_name} id:{product_id}\n')

def read_user_list():
    '''Criar uma lista com os usuários disponíveis e suas informações'''
    users = []
    with open('users.csv') as file:
            reader = csv.DictReader(file) #para usar o header como chave
            for row in reader:
                users.append(row)
    logs.write('Products list created\n')
    return users

def read_product_list():
    '''criar uma lista com os produtos disponíveis e suas informações'''

    products = []
    with open('products.csv') as file:
            reader = csv.DictReader(file) #para usar o header como chave
            for row in reader:
                products.append(row)
    logs.write('Products list created\n')
    return products

def update_users(users):
    '''Reescreve a lista de usuários para atualizar dados'''

    with open('users.csv','w') as file:
        file.write('id,user,password,permission\n')
        for i in range(len(users)):
            file.write(f'{users[i]["id"]},{users[i]["user"]},{users[i]["password"]},{users[i]["permission"]}')
            if i < len(users) - 1:
                file.write('\n')
    
    logs.write('Products updated\n')

def update_products(products):
    '''Reescreve a lista de produtos para atualizar dados'''

    with open('products.csv','w') as file:
        file.write('id,name,price,amount\n')
        for i in range(len(products)):
            file.write(f'{products[i]["id"]},{products[i]["name"]},{products[i]["price"]},{products[i]["amount"]}\n')
            if i < len(products) - 1:
                file.write('\n')
    
    logs.write('Products updated\n')

def delete_product(product_id):
    '''função para apagar produtos. '''

    ind, products = get_product_index(product_id)
    
    #deletar item
    del(products[ind])

    update_products(products)

    logs.write(f'product {product_id} deleted\n')

def delete_user(user_id):
    '''função para apagar usuário. '''

    ind, users = get_users_index(user_id)
    
    #deletar item
    del(users[ind])
    print(users)
    update_users(users)

    logs.write(f'user {user_id} deleted\n')

#utilities-------------------------------------------------------------------------

def while_option(minimum=False,maximum=False,isFloat=False):
    '''Escolher opção nos menus, achei importante fazer isso para o programar não crashar se escolher uma opção inválida, como escrever letras ou símbolos'''
    option = 0
    while True:
        option = input('')
        try:
            if not isFloat:
                option = int(option)
            else:
                option = float(option)

            if minimum:
                if option < minimum:
                    print('Opção inválida');print('')
                    continue 
            if maximum:
                if option > maximum:
                    print('Opção inválida');print('')
                    continue
            break
        except ValueError:
            print('Opção inválida')
    return option

def verify_user_id(user_id):
    '''Verifica de id de usuário existe'''
    while True:
        users = read_user_list()
        if user_id not in (i['id'] for i in users):
            print('id não encontrado')
            option = input('Quer tentar novamente?[s/n]: ')
            if option.lower().strip() == 'n':
                return False
            else:
                user_id = input('Digite o ID novamente: ')
                continue
        else:
            return True

def verify_product_id(product_id):
    '''Verifica se id de produto existe'''
    while True:
        products = read_product_list()
        if product_id not in (i['id'] for i in products):
            print('id não encontrado')
            option = input('Quer tentar novamente?[s/n]: ')
            if option.lower().strip() == 'n':
                return False
            else:
                product_id = input('Digite o ID novamente: ')
                continue
        else:
            return True

def get_users_index(user_id):
    '''Pegar o índice de usuário na lista'''

    users = read_user_list()
    i = 0
    for user in users:
        if user['id'] == user_id:
            break
        i += 1

    return i, users

def get_product_index(product_id, create_list=True):
    '''Pegar o índice de produto na lista'''

    products = read_product_list()
    i = 0
    for product in products:
        if product['id'] == product_id:
            break
        i += 1
    if create_list:
        return i, products
    else:
        return i

def program_exit():
    '''função para sair do programa de forma segura'''

    logs.write('program exit')
    logs.close()
    quit()

#program init----------------------------------------------------------------------
if __name__ == '__main__':
    create_files()
    Login()
    program_exit()