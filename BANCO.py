menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite aqui o valor do deposito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Você fez um deposito de: R$ {valor:.2f}\n"
            
        else:
            print("Falha na operação, o valor informado é inválido")
            
    elif opcao == 's':
        valor = float(input("Digite aqui o valor que pretende sacar: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente")
        
        elif excedeu_limite:
            print("Operação falhou! O valor do saque é maior que o valor do limite!")
            
        elif excedeu_saques:
            print("Operação falhou, pois ultrapassou o limite máximo de saques")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
        
        else:
            print("Operação falhou! O valor informado é inválido")
            
    elif opcao == "e":
        print("\n ================ EXTRATO ================")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("=============================================")
        
    elif opcao == "q":
        break
        
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")
