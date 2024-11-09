class Initialize():
    # banco de dados em memória (lista, em python)
    def __init__(self):
        self.__transactions = []

    def show_menu(self):
        print(50 * '-')
        print('Bem-vindo ao Controle Financeiro.')
        print(50 * '-')
        print('1 - Adicionar transação.')
        print('2 - Visualizar transações')
        print('3 - Sair')

    def choose_option(self):
        option = input('\nEscolha uma das opções: ')
        attemps = 0

        while not self.__check_option(option) and attemps < 10:
            attemps += 1
            print('\nOpção inválida!')
            option = input('Escolha uma das opções: ')

        return option

    def __check_option(self, option):
        return option in ['1', '2', '3']

    def __persist_transact(self, operation, value, description):
        self.__transactions.append(
            (operation, value, description)
        )
    
    def __retrieve_transactions_data(self):
        transact_data = []
        for transaction in self.__transactions:
                    transact_data.append((f'\nOperação: {transaction[0]} - '
                                          f'Valor: {transaction[1]} - '
                                          f'Descrição: {transaction[2]}.'))
        return transact_data

    def to_add(self):
        operation = input('Informar o tipo de operação: ')
        value = input('Informar o valor: ')
        description = input('Informe a descrição: ')
        # para garantir o encapsulamento, os métodos públicos não devem executar esse tipo de ação
        # pois facilita aos hackers efetuarem uma SQL Injection, por exemplo. É preciso que métodos
        # públicos chamem os métodos privados responsáveis por fazer isso
        
        self.__persist_transact(operation, value, description)

    def to_view(self):
        transact_data = self.__retrieve_transactions_data()
        for transaction in transact_data:
            print(transaction)

    def to_go_out(self):
        print('\nObrigado. Volte sempre!')


if __name__ == '__main__':
    init = Initialize()
    option = ''

    while option != '3':
        init.show_menu()
        option = init.choose_option()

        if option == '1':
            init.to_add()
        elif option == '2':
            init.to_view()
        elif option == '3':
            init.to_go_out()
    
