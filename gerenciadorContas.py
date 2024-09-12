from Estruturas.avlTree import AVLTree
from Estruturas.listaEncadeada import Lista

class Conta:
    def __init__(self, numero: str, saldo: float = 0):
        '''
        Inicializa uma conta com número e saldo.
        '''
        self.numero = numero
        self.saldo = saldo
        self.historico = Lista()  # Histórico utilizando lista encadeada

    def depositar(self, valor: float):
        '''
        Deposita um valor na conta e adiciona a transação ao histórico.
        '''
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo")
        self.saldo += valor
        self.historico.inserir(f"Depósito: {valor}")

    def sacar(self, valor: float):
        '''
        Saca um valor da conta e adiciona a transação ao histórico.
        '''
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente")
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo")
        self.saldo -= valor
        self.historico.inserir(f"Saque: {valor}")

    def transferir(self, valor: float, conta_destino: 'Conta'):
        '''
        Transfere um valor para outra conta e adiciona a transação ao histórico.
        '''
        if not isinstance(conta_destino, Conta):
            raise TypeError("O destino deve ser uma instância de Conta")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente")
        if conta_destino == self:
            raise ValueError("Não é possível transferir para a mesma conta")
        if valor <= 0:
            raise ValueError("O valor da transferência deve ser positivo")
        
        self.saldo -= valor
        self.historico.inserir(f"Transferência para conta {conta_destino.numero}: {valor}")
        
        conta_destino.saldo += valor
        conta_destino.historico.inserir(f"Transferência da conta {self.numero}: {valor}")
    
    def exibeHistorico(self) -> str:
        return self.historico.imprimir()

    def __str__(self):
        return f'Conta {self.numero}: Saldo {self.saldo}'

class GerenciadorContas:
    def __init__(self):
        '''
        Inicializa o gerenciador de contas com uma árvore AVL
        '''
        self.__contas = AVLTree()

    def criar_conta(self, numero, saldo):
        '''
        Cria uma nova conta e adiciona à árvore de contas
        '''
        if self.__contas.search(numero):
            return "Conta já existe"
        if saldo <= 0:
            return "Saldo inicial deve ser positivo"
        
        conta = Conta(numero, saldo)
        self.__contas.insert(conta)  # Insere o objeto Conta na árvore AVL
        conta.historico.inserir(f"Déposito inicial de: {saldo}.")
        return "Conta criada com sucesso"

    def consultar_saldo(self, numero):
        '''
        Consulta o saldo de uma conta
        '''
        conta = self.__contas.search(numero)
        if conta:
            return f"Saldo da conta {conta.numero}: {conta.saldo}"
        else:
            return "Conta não encontrada."

    def depositar(self, numero, valor):
        '''
        Deposita um valor na conta informada
        '''
        conta = self.__contas.search(numero)
        if isinstance(conta, Conta):
            conta.depositar(valor)
            return "Depósito realizado com sucesso"
        return "Conta não encontrada"

    def sacar(self, numero, valor):
        '''
        Saca um valor da conta especificada
        '''
        conta = self.__contas.search(numero)
        if isinstance(conta, Conta):
            try:
                conta.sacar(valor)
                return "Saque realizado com sucesso."
            except ValueError as e:
                return str(e)
        return "Conta não encontrada"

    def transferir(self, numero_origem: str, numero_destino: str, valor: float):
        '''
        Transfere um valor de uma conta para outra
        '''
        conta_origem = self.__contas.search(numero_origem)
        conta_destino = self.__contas.search(numero_destino)
        
        if conta_origem and conta_destino:
            try:
                conta_origem.transferir(valor, conta_destino)
                return f"Transferência de {valor} realizada da conta {numero_origem} para a conta {numero_destino}."
            except (ValueError, TypeError) as e:
                return str(e)
        else:
            return "Uma ou ambas as contas não foram encontradas."

    def historico(self, numero):
        '''
        Retorna o histórico de transações de uma conta
        '''
        conta = self.__contas.search(numero)
        if conta:
            return conta.exibeHistorico()
        return "Conta não encontrada."