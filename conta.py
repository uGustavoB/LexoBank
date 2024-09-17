from Estruturas.PilhaEncadeada import Pilha

class Conta:
    def __init__(self, numero: str, saldo: float = 0):
        '''
        Inicializa uma conta com número e saldo.
        '''
        self.numero = numero
        self.saldo = saldo
        self.historico = Pilha()  # Histórico utilizando pilha encadeada

    def depositar(self, valor: float):
        '''
        Deposita um valor na conta e adiciona a transação ao histórico.
        '''
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo")
        self.saldo += valor
        self.historico.empilha(f"Depósito: {valor}")

    def sacar(self, valor: float):
        '''
        Saca um valor da conta e adiciona a transação ao histórico.
        '''
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente.")
        if valor <= 0:
            raise ValueError("O valor do saque deve ser maior que zero.")
        self.saldo -= valor
        self.historico.empilha(f"Saque: {valor}")

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
        self.historico.empilha(f"Transferência para conta {conta_destino.numero}: {valor}")
        
        conta_destino.saldo += valor
        conta_destino.historico.empilha(f"Transferência da conta {self.numero}: {valor}")
    
    def exibeHistorico(self) -> str:
        return self.historico

    def __str__(self):
        return f'Conta {self.numero}: Saldo {self.saldo}'