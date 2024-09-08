import socket
from Estruturas.avlTree import AVLTree
from Estruturas.hashTable import HashTable
from Estruturas.listaEncadeada import Lista

'''
A classe 'BankServer' cuida de várias operações bancárias, como criar contas, consultar saldos, fazer depósitos e saques, e até mesmo transferências entre contas.

Para organizar tudo isso:
- Usamos uma árvore AVL para gerenciar as contas.
- Utilizamos uma tabela hash para controlar os saldos de cada conta.
- Mantemos um histórico de transações com uma lista encadeada.
'''
class BankServer:
    def __init__(self, host="localhost", port=9999):
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind((host, port)) # Associando o servidor ao endereço e porta
            self.server.listen(5) # Servidor configurado para escutar até 5 conexões. Se for alterar tem que verificar se afeta o desempenho
                                  # Pra que ele atenda os 5 ao mesmo, tem que implementar threads, mas não é requisito
            print("Servidor de banco iniciado com sucesso.")
        except Exception as e:
            print(f"Erro ao iniciar o servidor: {e}")
            exit()

        self.avlTree = AVLTree()
        self.hashTable = HashTable()
        self.transacoes = Lista()  # Armazena o histórico de transações

    def start(self):
        while True:
            try:
                clientSocket, addr = self.server.accept()
                print(f"Conexão estabelecida com {addr}")

                while True:
                    try:
                        request = clientSocket.recv(4096).decode()
                        if not request:
                            print(f"Cliente {addr} desconectado.")
                            break
                        response = self.handleRequest(request)
                        clientSocket.send(response.encode())
                    except Exception as e:
                        print(f"Erro durante a comunicação com o cliente {addr}: {e}")
                        break
                clientSocket.close()
                print(f"Conexão com {addr} fechada.")
            except Exception as e:
                print(f"Erro ao aceitar conexão: {e}")

    def handleRequest(self, request):
        tokens = request.split()
        command = tokens[0]

        if command == "CREATE":
            accountNumber = tokens[1]
            balance = float(tokens[2])
            if self.avlTree.search(accountNumber):
                return "Erro: Conta já existe."
            self.avlTree.insert(accountNumber)
            self.hashTable.insert(accountNumber, balance)
            self.transacoes.inserir(len(self.transacoes) + 1, f"CREATE {accountNumber} {balance}")
            return f"Conta {accountNumber} criada com sucesso."

        elif command == "BALANCE":
            accountNumber = tokens[1]
            balance = self.hashTable.search(accountNumber)
            if balance is not None:
                return f"Saldo da conta {accountNumber}: {balance}"
            else:
                return "Conta não encontrada."

        elif command == "DEPOSIT":
            accountNumber = tokens[1]
            amount = float(tokens[2])
            current_balance = self.hashTable.search(accountNumber)
            if current_balance is not None:
                new_balance = current_balance + amount
                self.hashTable.update(accountNumber, new_balance)
                self.transacoes.inserir(len(self.transacoes) + 1, f"DEPOSIT {accountNumber} {amount}")
                return f"Depósito de {amount} realizado. Novo saldo: {new_balance}."
            else:
                return "Conta não encontrada."

        elif command == "WITHDRAW":
            accountNumber = tokens[1]
            amount = float(tokens[2])
            current_balance = self.hashTable.search(accountNumber)
            if current_balance is not None:
                if current_balance >= amount:
                    new_balance = current_balance - amount
                    self.hashTable.update(accountNumber, new_balance)
                    self.transacoes.inserir(len(self.transacoes) + 1, f"WITHDRAW {accountNumber} {amount}")
                    return f"Saque de {amount} realizado. Novo saldo: {new_balance}."
                else:
                    return "Saldo insuficiente."
            else:
                return "Conta não encontrada."

        elif command == "TRANSFER":
            accountNumberFrom = tokens[1]
            accountNumberTo = tokens[2]
            amount = float(tokens[3])

            balance_from = self.hashTable.search(accountNumberFrom)
            balance_to = self.hashTable.search(accountNumberTo)

            if balance_from is None:
                return "Conta de origem não encontrada."
            if balance_to is None:
                return "Conta de destino não encontrada."

            if balance_from < amount:
                return "Saldo insuficiente para transferência."

            new_balance_from = balance_from - amount
            new_balance_to = balance_to + amount

            self.hashTable.update(accountNumberFrom, new_balance_from)
            self.hashTable.update(accountNumberTo, new_balance_to)

            self.transacoes.inserir(len(self.transacoes) + 1, f"TRANSFER {accountNumberFrom} {accountNumberTo} {amount}")

            return f"Transferência de {amount} de {accountNumberFrom} para {accountNumberTo} realizada com sucesso."

        elif command == "HISTORY":
            history = str(self.transacoes)
            return history if history else "Nenhuma transação encontrada."

        else:
            return "Comando inválido."
        
if __name__ == "__main__":
    server = BankServer()
    server.start()