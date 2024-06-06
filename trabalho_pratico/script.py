import csv
import os

logs = open('logs.txt','w')

def create_files():
    '''criar arquivos necessários se não existirem'''

    path = os.getcwd()
    if not os.path.exists(f'{path}/products.csv'):
        with open('products.csv','w') as file:
            file.write('id,name,price,amount')
    if not os.path.exists(f'{path}/users.csv'):
        with open('users.csv','w') as file:
            file.write('id,user,password,permition\n0,owner,00000,3')
    
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
        
def Main(id, user, permition):
    '''onde o usuário escolherá o que fazer'''

    print(f'Bem-vindo(a) {user}!')

    #só vai sair quando o usuário pedir
    while True:
        maximum = 2
        print('O que você gostaria de fazer?');print('')
        print('[0]sair - [1]trocar usuário - [2]caixa',end=' ')

        #permissões para pessoas com cargo maior
        if permition > 1:
            maximum = 3
            print(' - [3]Gerenciar produtos', end='')

        print('')

        option = while_option(0,maximum)

        if option == 0:
            program_exit()
        elif option == 1:
            logs.write(f'user {id} left')
            Login()
            break
        elif option == 2:
            cashier(id, user)
        elif permition > 1 and option == 3:
            management(id, user)
        else:
            print('Opção inválida')

def management(id, user):
    '''onde dados dos produtos podem ser alterados'''

    logs.write('went to management function\n')

    while True:
        print('O que deseja fazer?');print('')
        print('[0]Voltar - [1]Criar - [2]Atualizar - [3]Deletar');print('')

        option = while_option(0,3)
        
        if option == 0:
            break
        #adicionar produto
        if option == 1:
            create_products()
        #modificar produto
        elif option == 2:
            while True:
                product_id = input('Digite o ID do produto: ')
                if verify_product_id(product_id):
                    print('O que deseja modificar?')
                    print('[0]Cancelar - [1]Nome - [2]Preço unitário - [3]Quantidade - [4]Todos')
                    
                    update_products_manager(product_id)

                option = input('Quer alterar outro produto?[s/n]: ')
                if option.lower().strip() == 'n':
                    break

        #deletar produto
        elif option == 3:
            while True:
                product_id = input('ID: ')
                if verify_product_id(product_id):
                    option = input('Tem certeza?[s/n]: ')
                    if option.lower().strip() == 's':
                        delete_products(product_id)    
                    else:
                        print('operação cancelada')

                option = input('Quer alterar outro produto?[s/n]: ')
                if option.lower().strip() == 'n':
                    break
            

        option = input('Quer continuar gerenciando?[s/n]: ')
        if option.lower().strip() == 'n':
            break

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
            while True:
                current_sell_product_list = []
            
                while True:
                    product_id = input('ID do produto: ')
                    if verify_product_id(product_id):
                        print('Qual a quantidade?: ')
                        sell_amount = while_option(0)
                        
                        ind, products = get_product_index(product_id)
                        
                        #ter certeza de existir a quantidade a ser vendida
                        product_amount = products[ind]['amount']
                        if sell_amount > int(product_amount):
                            print('Está tentando vender mais do que há no estoque')
                            continue

                        product_price = products[ind]['price']

                        #preço total da venda
                        sell_price = sell_amount * float(product_price)
                        
                        #adicionar dados da compra do produto na lista
                        current_sell_product_list.append({
                            'id':product_id,
                            'name':products[ind]['name'],
                            'amount':sell_amount,
                            'sell_price':sell_price
                        })

                    logs.write(f'New product added to the list: {current_sell_product_list}')
                    
                    option = input('Quer digitar outro ID?[s/n]: ')
                    if option.lower().strip() == 'n':
                        update_amount(current_sell_product_list)
                        break
                
                logs.write('Products sold!\n')

                option = input('Quer realizar outra venda?[s/n]: ')
                if option.lower().strip() == 'n':
                    break
        else:
            print('Opção inválida')
        

def update_amount(product_list):
    '''Para dar update na quantidade dos produtos vendidos no caixa. Decidi deixar separado para que o código fique mais claro'''
    
    products = read_product_list()
    for item in product_list:
        product_id = item['id']

        ind, tmp = get_product_index(product_id)
        
        products[ind]['amount'] = int(products[ind]['amount']) - int(item['amount'])

    update_products(products)
    

#CRUD--------------------------------------------------------------------------------------------

def create_products():
    '''Função para criar produtos'''

    print('insira os dados do produto')
    while True:
        product_id = input('ID: ')
        products = read_product_list()
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

    logs.write(f'created product {product_name} id:{product_id}\n')

def read_product_list():
    '''criar uma lista com os produtos disponíveis e suas informações'''

    products = []
    with open('products.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append(row)
    logs.write('Products list created\n')
    return products

def update_products(products):
    '''Reescreve a lista de produtos para atualizar dados'''

    with open('products.csv','w') as file:
        file.write('id,name,price,amount\n')
        for product in products:
            file.write(f'{product["id"]},{product["name"]},{product["price"]},{product["amount"]}\n')
    
    logs.write('Products updated\n')

def update_products_manager(product_id,new_name=False,new_price=False,new_amount=False):
    '''função para atualizar dados. 
    Todos estão com falso como padrão, assim só será modificado os valores que forem passados'''

    #escolher o que quer trocar
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

def delete_products(product_id):
    '''função para apagar produtos. '''

    ind, products = get_product_index(product_id)
    
    #deletar item
    del(products[ind])

    update_products(products)

    logs.write(f'product {product_id} deleted\n')

#utilities-------------------------------------------------------------------------

def while_option(minimum=False,maximum=False):
    '''Escolher opção nos menus, achei importante fazer isso para o programar não crashar se escolher uma opção inválida, como escrever letras ou símbolos'''
    option = 0
    while True:
        option = input('')
        if option.isdigit():
            option = int(option)

            if minimum:
                if option < minimum:
                    print('Opção inválida')
                    continue 
            if maximum:
                if option > maximum:
                    print('Opção inválida')
                    continue
            break
        else:
            print('Opção inválida')
    return option

def verify_product_id(product_id):
    '''Verifica se id existe'''
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

def get_product_index(product_id):
    '''Estava repetindo muito isso, então tranformei em função'''

    products = read_product_list()
    i = 0
    for product in products:
        if product['id'] == product_id:
            break
        i += 1
    return i, products

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