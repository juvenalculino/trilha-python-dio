import textwrap
'''
Parte 1:
separar as funções existentes de saque, deposito e extrato em funções.
Criar duas novas funcoes: cadastrar usuario (cliente) e cadastrar conta bancaria.
Parte 2:
Precisamos deixar nosso código mais modilarizado, para iddo vamos criar funções
para as operações existentes: sacar, depositar e visualizar histórico.
Além disso, para a versão 2 do nosso sistema precisamos criar duas novas
funções: Criar usuário (cliente do banco) e criar conta corrente vinculada ao usuário.
'''
def menu():
    menu = '''\n
    =============MENU=============
    [d]\t Depositar
    [s]\t Sacar
    [e]\t Extrato
    [nc]\t Nova Conta
    [lc]\t Listar Contas
    [nu]\t Novo Usuário
    [q]\t Sair
    '''
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Deposito R${valor:.2f}\n'
        print('\n=== Depósito realizado com sucesso! ===')
    else:
        print('\n@@@ Operação falhou! O valor informado é inválido. @@@')
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saques > limite_saques
    
    if excedeu_saldo:
        print('\n@@@ Operação falhou! você não tem saldo suficiente. @@@')
    elif excedeu_limite:
        print('\n@@@ Operação falhou! O valor do saque excede o limite. @@@')
    elif excedeu_saque:
        print('\n@@@ Operação falhou! Número máximo de saques excedido. @@@')
    
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque R${valor:.2f}\n'
        numero_saques += 1
        print('\n=== Saque realizado com sucesso! ===')
    else:
        print('\n@@@ Operação falhou! O valor informado é inválido. @@@')
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o seu CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Parece que já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o seu nome completo: ")
    data_nascimento = input("Informe a data do seu nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o seu endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuario):
    usuario_filtrado = [user for user in usuario if user['cpf'] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None

def criar_conta(agencia, num_conta, usuario):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuario)

    if usuario:
        print('\n@@@ Usuário criado com sucesso. @@@')
        return {"agencia": agencia, "num_conta": num_conta, "usuario": usuario}
    print('\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado. @@@')
        

def listar_conta(contas):
    for conta in contas:
        linha = f"""\
            Agência: {conta['agencia']}
            C/C: {conta['num_conta']}
            Titular: {conta['usuario']['nome']}
        """
        print('=' * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = '001'

    saldo = 0
    limite = 500
    extrato = ''
    numero_conta = 0
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input('Digite o valor a ser depositado: '))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao =='s':
            valor = float(input('Digite o valor a ser sacado: '))
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES,)

        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == 'nu':
            criar_usuario(usuarios)
        
        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                conta.append(contas)
        elif opcao == 'lc':
            listar_conta(contas)
        
        elif opcao == 'q':
            break



main()
