import socket
from Estruturas.listaEncadeada import Lista
import subprocess
import time

'''
Todos os "time.sleep()" é usada para pausar por um determinado tempo, foi adicionado para que seja possível ler o retorno do servidor
'''
class BackCliente:
    def __init__(self, host="localhost", port=9999):
        # Inicializa o socket e a conexão com o servidor
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        self.transacoes = Lista()  # Para armazenar histórico de transações
    
    def enviar_requisicao(self, requisicao):
        self.client.send(requisicao.encode())
        resposta = self.client.recv(4096).decode()
        print(resposta)
        
        # Adiciona a transação ao histórico na última posição
        self.transacoes.inserir(len(self.transacoes) + 1, requisicao)
    
    def fechar_conexao(self):
        self.client.close()
    
    # Futura implementação - Limpar o terminal independente do sistema operacional. Atualmente só está limpando o terminal se for Windows
    # def limpar_terminal(self):

if __name__ == "__main__":
    cliente = BackCliente()

    while True:
        subprocess.call('cls', shell=True)  # Limpa o terminal a cada interação
        print("1. Criar Conta")
        print("2. Consultar Saldo")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Transferir")
        print("6. Histórico de Transações")
        print("7. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            numero_conta = input("Número da conta: ")
            saldo = input("Saldo inicial: ")
            cliente.enviar_requisicao(f"CREATE {numero_conta} {saldo}")
            time.sleep(2) 

        elif escolha == "2":
            numero_conta = input("Número da conta: ")
            cliente.enviar_requisicao(f"BALANCE {numero_conta}")
            time.sleep(2) 

        elif escolha == "3":
            numero_conta = input("Número da conta: ")
            valor = input("Valor do depósito: ")
            cliente.enviar_requisicao(f"DEPOSIT {numero_conta} {valor}")
            time.sleep(2)

        elif escolha == "4":
            numero_conta = input("Número da conta: ")
            valor = input("Valor do saque: ")
            cliente.enviar_requisicao(f"WITHDRAW {numero_conta} {valor}")
            time.sleep(2)

        elif escolha == "5":
            conta_origem = input("Número da conta de origem: ")
            conta_destino = input("Número da conta de destino: ")
            valor = input("Valor da transferência: ")
            cliente.enviar_requisicao(f"TRANSFER {conta_origem} {conta_destino} {valor}")
            time.sleep(4)

        elif escolha == "6":
            cliente.enviar_requisicao("HISTORY")
            time.sleep(4) 

        elif escolha == "7":
            cliente.fechar_conexao()
            break

        else:
            print("Opção inválida.")
            time.sleep(2)  