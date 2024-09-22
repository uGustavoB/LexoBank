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
            return 306, None
        self.saldo += valor
        self.historico.empilha(f"Depósito: {valor}")
        return 200, None  # Operação bem-sucedida

    def sacar(self, valor: float):
        '''
        Saca um valor da conta e adiciona a transação ao histórico.
        '''
        if valor > self.saldo:
            return 304, None
        if valor <= 0:
            return 307, None
        self.saldo -= valor
        self.historico.empilha(f"Saque: {valor}")
        return 200, None  # Operação bem-sucedida

    # def transferir(self, valor: float, conta_destino: 'Conta'):
    #     '''
    #     Transfere um valor para outra conta e adiciona a transação ao histórico.
    #     '''
    #     if not isinstance(conta_destino, Conta):
    #         return 302, None
    #     if valor > self.saldo:
    #         return 304, None
    #     if conta_destino == self:
    #         return 303, None
    #     if valor <= 0:
    #         return 308, None
        
    #     self.saldo -= valor
    #     self.historico.empilha(f"Transferência para conta {conta_destino.numero}: {valor}")
        
    #     conta_destino.saldo += valor
    #     conta_destino.historico.empilha(f"Transferência da conta {self.numero}: {valor}")
    
    def exibeHistorico(self) -> str:
        return self.historico

    def __str__(self):
        return f'Conta {self.numero}: Saldo {self.saldo}'