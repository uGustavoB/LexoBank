from bankClient import BankClient
import os

if __name__ == "__main__":
    # Cria uma instância do cliente do banco
    cliente = BankClient()

    # Verificia se a conexão com o servidor foi estabelecida
    if cliente.cliente:
        while True:
            # Limpa o terminal a cada interação para uma melhor visualização
            if os.name == 'nt': # Para Windows
                os.system('cls')
            else: # Para sistemas baseado em Unix (Linux, macOS)
                os.system('clear')

            # Exibe o menu de opções se a conexão foi estabelecida
            print("1. Criar Conta")
            print("2. Consultar Saldo")
            print("3. Depositar")
            print("4. Sacar")
            print("5. Transferir")
            print("6. Histórico de Transações")
            print("7. Sair")

            escolha = input("Escolha uma opção: ")

            try:
                # Executa a opção escolhida pelo usuário
                if escolha == "1":
                    numero_conta = input("Número da conta: ")
                    saldo = input("Saldo inicial: ")
                    
                    cliente.enviar_requisicao(f"CREATE {numero_conta} {saldo}") # Envia uma requisão ao servidor para criar uma nova conta
                    cliente.pausa_interacao()

                elif escolha == "2":
                    numero_conta = input("Número da conta: ") 
                    cliente.enviar_requisicao(f"BALANCE {numero_conta}") # Envia uma requisição ao servidor para consultar o saldo da conta fornecida
                    cliente.pausa_interacao() # Pausa a interação para que o usuário possa ver a resposta antes de continuar
                    # Pode ser substituído por input("Pressione Enter para continuar...")

                elif escolha == "3":
                    numero_conta = input("Número da conta: ")
                    valor = input("Valor do depósito: ")
                    cliente.enviar_requisicao(f"DEPOSIT {numero_conta} {valor}") # Envia uma requisição ao servidor para depositar o valor na conta fornecida
                    cliente.pausa_interacao()

                elif escolha == "4":
                    numero_conta = input("Número da conta: ")
                    valor = input("Valor do saque: ")
                    cliente.enviar_requisicao(f"WITHDRAW {numero_conta} {valor}") # Envia uma requisição ao servidor para sacar o valor da conta fornecida
                    cliente.pausa_interacao()

                elif escolha == "5":
                    conta_origem = input("Número da conta de origem: ")
                    conta_destino = input("Número da conta de destino: ")
                    valor = input("Valor da transferência: ")
                    cliente.enviar_requisicao(f"TRANSFER {conta_origem} {conta_destino} {valor}") # Envia uma requisição ao servidor para transferir o valor da conta de origem para a conta de destino
                    cliente.pausa_interacao()

                elif escolha == "6":
                    numero_conta = input("Número da conta: ")
                    cliente.enviar_requisicao(f"HISTORY {numero_conta}") # Envia uma requisição ao servidor para obter o histórico de transações da conta fornecida
                    cliente.pausa_interacao()

                elif escolha == "7":
                    # Fecha a conexão e encerra o loop
                    cliente.fechar_conexao()
                    break

                else:
                    print("Opção inválida.")
                    cliente.pausa_interacao()

            except Exception as e:
                # Captura e exibe erros inesperado
                print(f"Erro: {e}")
                cliente.pausa_interacao()