'''
Deve ser possível depositar valores positivos
Todos os depositos devem ser armazenados em uma variavel e exibidos na operação de extrato
O sistema deve permitir realizar 3 saques diários com limite maximo de R$ 500.
Caso o cliente não tenha saldo em conta o sistema deve exibir uma mensagem informando que não será possível  sacar o dinheiro por
Todos os saques devem ser armazenados em uma variavel e exibidos na operação de extrato
'''

menu = '''
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == 'd':
        valor = float(input('Digite o valor a ser depositado: '))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito de R$ {valor:.2f}\n'
        else:
            print('Valor inválido')

    elif opcao == 's':
        valor = float(input('Digite o valor a ser sacado: '))
        if valor > saldo:
            print('Saldo insuficiente')
        elif valor > limite:
            print('Valor de saque excede o limite.')
        elif numero_saques >= LIMITE_SAQUES:
            print('Limite de saques excedido.')
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque de R$ {valor:.2f}\n'
            numero_saques += 1
            
    elif opcao == 'e':
        print(f'Saldo: R$ {saldo:.2f}')
        print('Não foi realizado movimentações.' if not extrato else extrato)
    elif opcao == 'q':
        print('Obrigado por utilizar nossos serviços!')
        break
        
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')
