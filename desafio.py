import textwrap

def menu():
    menu = """
    ==============#
    [D]  Depositar
    [S]  Sacar
    [E]  Extrato
    [NC] Nova conta corrente
    [NU] Novo usuário
    [X]  Sair
    ==============#
    
    Escolha uma opção: """
    return input(textwrap.dedent(menu)).lower()


def deposito(saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Valor inválido.")

    return saldo, extrato


def saque( saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES, /):

    if valor <= 0:
        print("Valor inválido.")

    elif valor > saldo:
        print("Saldo insuficiente.")

    elif valor > limite:
        print("Valor excede o limite.")

    elif numero_saques >= LIMITE_SAQUES:
        print("Saques diários esgotados.")

    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    return saldo, extrato


def mostrar_extrato(saldo, extrato, /):
    print("\nExtrato: ")
    print("Extrato vazio.\n" if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    input('\nEnter para continuar.')


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (apenas números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nUsuario já existe.\n")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado.")

def app():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Valor do depósito: "))
            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Valor do saque: "))

            saldo, extrato = saque(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES)

        elif opcao == "e":
            mostrar_extrato(saldo, extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "x":
            break

        else:
            print("Escolha inválida.")

app()
