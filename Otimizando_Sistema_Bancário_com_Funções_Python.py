menu = """
=============================
|| Operações:              ||
|| [d]  Deposito           ||
|| [s]  Saque              ||
|| [e]  Extrato            ||
|| [Nc] Nova Conta         ||
|| [Lc] Listar clinte      ||
|| [Nu] Novo Usuário       ||
|| [x]  Sair               ||
=============================
>>>>"""

def depositar(saldo, valor_do_deposito, extrato,/):
    deposito_invalido ="\nErro, valor informado não é válido. Informe um valor válido."
    if valor_do_deposito > 0:
        saldo += valor_do_deposito
        extrato += f"Depósito: R$ {valor_do_deposito:.2f}\n"
    else:
        print(deposito_invalido)
    return saldo, extrato

def sacar(*, saldo, valor_do_saque, extrato, valor_maximo_de_saque, saques_diarios):

    saldo_insuficiente = "\nNão foi possível realizar o saque. Saldo insuficiente."
    saque_excedeu_limite = "\nNão foi possível realizar o saque. O valor do saque excedeu o limite."
    limite_de_saques_alcancado = "\nNão foi possível realizar o saque. Número máximo de saques do dia alcançado."
    saque_invalido = "\nNão foi possível realizar o saque. O valor informado é inválido."

    if valor_do_saque > saldo:
        print(saldo_insuficiente)

    elif valor_do_saque > valor_maximo_de_saque:
        print(saque_excedeu_limite)
            
    elif saques_diarios == 0:
        print(limite_de_saques_alcancado)
            
    elif valor_do_saque > 0:
        saldo -= valor_do_saque
        extrato += f"Saque: R$ {valor_do_saque: .2f}\n"
        saques_diarios -= 1
            
    else:
        print(saque_invalido)

    return saldo, extrato, saques_diarios

def mostrar_extrato(saldo,/,*,extrato):
    print("\n=========================================\n"
        "================ EXTRATO ================\n")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=========================================\n" \
        "=========================================")

def criar_novo_usuario(clientes):
    CPF = input("\nPor favor! Informe o CPF do cliente: ")
    cliente = filtrar_clientes(CPF, clientes)
    
    if cliente:
        print("\n######CLIENTE JÁ CADASTRADO!######")
        return 
    
    nome = input("\nNome completo: ")
    data_de_nascimento = input("Data de nascimento(dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, número - bairro - cidade/sigla do estado): ")

    clientes.append({"nome": nome, "data_nascimento": data_de_nascimento, "cpf": CPF, "endereco": endereco})

    print("\n######Cliente cadastrado!######")

def filtrar_clientes(CPF, clientes):
    usuarios_filtrados = [usuario for usuario in clientes if usuario["cpf"] == CPF]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_contas(agencia, numero_da_conta, clientes):
    CPF = input("\nInforme o CPF do usuário: ")
    cliente = filtrar_clientes(CPF,clientes)

    if cliente:
        print("\nConta criada!")
        return {"agencia": agencia, "numero_conta": numero_da_conta, "usuario": cliente}
    print("\nUSUÁRIO NÃO FOI ENCONTRADO!!!!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
Agência:{conta['agencia']}
C/C:{conta['numero_conta']}
Titular:{conta['usuario']['nome']}"""
        print(linha)

def funcao_principal():
    operacao_invalida ="\nOperação informada inválida, por favor selecione novamente a operação." 

    agencia = "0001"
    extrato = ""
    saldo = 0
    saques_diarios = 3
    valor_maximo_de_saque = 500.00
    clientes = []
    contas = []

    operacao = input(menu)

    while operacao != "x":

        if operacao == "d":
            valor_do_deposito = float(input("\nInforme o valor do depósito: "))
            saldo,extrato = depositar(saldo,valor_do_deposito,extrato)
        
        elif operacao == "s":
            valor_do_saque = float(input("\nInforme o valor do saque: "))
            saldo,extrato,saques_diarios = sacar(
                saldo=saldo,
                valor_do_saque=valor_do_saque,
                extrato=extrato,
                valor_maximo_de_saque=valor_maximo_de_saque,
                saques_diarios=saques_diarios
            )

        elif operacao == "e":
            mostrar_extrato(saldo, extrato=extrato)

        elif operacao == "Nu":
            criar_novo_usuario(clientes)

        elif operacao == "Nc":
            numero_da_conta = len(contas) + 1
            conta = criar_contas(agencia, numero_da_conta, clientes)

            if conta:
                contas.append(conta)

        elif operacao == "Lc":
            listar_contas(contas)

        else:
            print(operacao_invalida)

        operacao = input(menu)

funcao_principal()