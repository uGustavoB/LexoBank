from bankClient import BankClient
import os

if __name__ == "__main__":
    '''
    Ponto de entrada do programa, que inicia a interação com o cliente do banco. 

    Este bloco cria uma instância da classe `BankClient` e permite que o usuário interaja com um menu de opções
    para realizar operações bancárias como criar conta, consultar saldo, depositar, sacar, transferir e visualizar 
    o histórico de transações.
    
    Exemplo de uso:
        Executar o script para iniciar a interação do cliente.
    '''
    
    host = input("Digite o endereço IP do servidor. Caso esteja rodando localmente, deixe em branco: ")
    
    cliente = BankClient(host=host)

    # Verificia se a conexão com o servidor foi estabelecida
    if cliente.cliente: # O atributo cliente da instância BankClient indica o status da conexão.
        while True:
            # Limpa o terminal a cada interação para uma melhor visualização para Windows e para sistemas baseado em Unix (Linux, macOS)
            if os.name == 'nt': 
                os.system('cls')
            else: 
                os.system('clear')

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
                    cliente.enviar_requisicao(f"CREATE {numero_conta} {saldo}")
                    cliente.pausa_interacao()

                elif escolha == "2":
                    numero_conta = input("Número da conta: ") 
                    cliente.enviar_requisicao(f"BALANCE {numero_conta}") 
                    cliente.pausa_interacao() 
                    # Pode ser substituído por input("Pressione Enter para continuar...")

                elif escolha == "3":
                    numero_conta = input("Número da conta: ")
                    valor = input("Valor do depósito: ")
                    cliente.enviar_requisicao(f"DEPOSIT {numero_conta} {valor}")
                    cliente.pausa_interacao()

                elif escolha == "4":
                    numero_conta = input("Número da conta: ")
                    valor = input("Valor do saque: ")
                    cliente.enviar_requisicao(f"WITHDRAW {numero_conta} {valor}") 
                    cliente.pausa_interacao()

                elif escolha == "5":
                    conta_origem = input("Número da conta de origem: ")
                    conta_destino = input("Número da conta de destino: ")
                    valor = input("Valor da transferência: ")
                    cliente.enviar_requisicao(f"TRANSFER {conta_origem} {conta_destino} {valor}") 
                    cliente.pausa_interacao()

                elif escolha == "6":
                    numero_conta = input("Número da conta: ")
                    cliente.enviar_requisicao(f"HISTORY {numero_conta}") 
                    cliente.pausa_interacao()

                elif escolha == "7":
                    cliente.fechar_conexao()
                    break  # encerra o loop e sai do menu

                else:
                    print("Opção inválida.")
                    cliente.pausa_interacao()

            except Exception:
                print(f"Erro de entrada: Lembre-se de que você deve inserir números válidos. Revise seus dados e tente novamente.")
                cliente.pausa_interacao()