saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

menu = """
==============#
[D] Depositar
[S] Sacar
[E] Extrato
[X] Sair
==============#
 """

while True:
    print(menu)
    opcao = input("Escolha uma opção: ").lower()

    if opcao == "d":
        valor = float(input("Valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Valor inválido.")

    elif opcao == "s":
        valor = float(input("Valor do saque: "))

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

    elif opcao == "e":
        print("\nExtrato: ")
        print("Extrato vazio.\n" if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        input('\nEnter para continuar.')

    elif opcao == "x":
        break

    else:
        print("Escolha inválida.")