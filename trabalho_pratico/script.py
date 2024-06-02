import csv

logs = open('logs.txt','w')

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
                logs.write(f'user {users[i]['id']} logged\n')
                Main(users[i]['id'], user_input, int(users[i]['permition']))
                break
            
            #se apos checar tudo não achar, sair
            if i >= len(users) - 1:
                print('credenciais inválidas')
                break
        
        option = input('Quer sair? [s/n]: ')
        if option.lower().strip() == 's':
            program_exit()
        
#onde o usuário escolherá o que fazer
def Main(id, user, permition):
    print(f'Bem-vindo(a) {user}!')

    while True:
        print('O que você gostaria de fazer?');print('')
        print('[0]sair - [1]trocar usuário - [2]caixa',end=' ')

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
            cashier()
            break
        elif permition > 1 and option == 3:
            management()
            break
        else:
            print('Opção inválida')

#onde dados dos produtos podem ser alterados
def management():
    logs.write('went to management function\n')
    products = create_product_list()
    print(products)

def cashier():
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
    return products

def program_exit():
    logs.write('program exit')
    logs.close()
    quit()

if __name__ == '__main__':
    Login()
    program_exit()