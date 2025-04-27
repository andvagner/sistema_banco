from winreg import EnableReflectionKey


menu = """
###### Menu de opções ######\n
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Digite uma das opções:"""

saldo = 0
limite = 10000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

mensagem_erro_deposito = "Operação Falhou! O valor informado é inválido."
mensagem_erro_saldo = "Operação falhou! Você não tem saldo suficiente"
mensagem_erro_limite = "Operação falhou! O valor do saque excedeu o limite"
mensagem_erro_saque = "Operação falhou! Número máximo de saques excedido."
mensagem_erro_opcao = "Operação inválida, por favor selecione novamenate a operação desejada"



while True:
    
    opcao = input(menu)
    if opcao == "d":
        
        valor_deposito = float(input("Informe o valor do depósito:"))
        
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f} + \n"
        else:
            print(mensagem_erro_deposito)
            
            
    elif opcao == "s":
        valor_saque = float(input("Informe o valor do saque:"))
        
        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print(mensagem_erro_saldo)
        elif excedeu_limite:
            print(mensagem_erro_limite)
        elif excedeu_saques:
            print(mensagem_erro_saque)
        
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f} - \n"
            numero_saques += 1
        
        else:
            print("Operação falhou! O valor informado é inválido.")
        
    elif opcao == "e":
        print("\n============= EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("========================================")
        
    elif opcao == "q":
        break
    
    else:
        print(mensagem_erro_opcao)


