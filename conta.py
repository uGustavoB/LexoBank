from Estruturas.PilhaEncadeada import Pilha

class Conta:
    '''
    Classe que representa uma conta bancária.

    Atributos:
        numero (str): O número da conta.
        saldo (float): O saldo atual da conta.
        historico (Pilha): O histórico de transações da conta.
    '''
    def __init__(self, numero: str, saldo: float = 0):
        '''
        Inicializa uma conta com número e saldo.

        Parâmetros:
            numero (str): O número da conta.
            saldo (float): O saldo inicial da conta (default é 0).
        '''
        self.numero = numero
        self.saldo = saldo
        self.historico = Pilha()  # Histórico utilizando pilha encadeada

    def depositar(self, valor: float):
        '''
        Método que deposita um valor na conta e adiciona a transação ao histórico.

        Parâmetros:
            valor (float): O valor a ser depositado

        Returns: 
            tuple: Um código indicando o resultado da operação e uma mensagem opcional.
            Códigos:
            - 200: Operação realizada com sucesso.
            - 306: O valor do depósito deve ser positivo

        Exemplos de uso:
            conta = Conta("12345", 1000.0)
            resultado = conta.depositar(500.0)
            print(resultado) # (200, None)
        '''
        if valor <= 0:
            return 306
        self.saldo += valor
        self.historico.empilha(f"Depósito: {valor}")
        return 200

    def sacar(self, valor: float):
        '''
        Saca um valor da conta e adiciona a transação ao histórico.

        Parâmetros:
            valor (float): O valor a ser sacado.
        
        Returns:
            tuple: Um código indicando o resultado da operação e uma mensagem opcional.
                Códigos:
                - 200: Operação realizada com sucesso.
                - 304: Saldo insuficiente
                - 307: O valor do saque deve ser maior que zero

        Exemplos de uso:
            conta = Conta("12345", 1000.0)
            resultado = conta.sacar(300.0)
            print(resultado)  # (200, None)
        '''
        if valor > self.saldo:
            return 304
        if valor <= 0:
            return 307
        self.saldo -= valor
        self.historico.empilha(f"Saque: {valor}")
        return 200
    
    def exibeHistorico(self) -> str:
        '''
        Retorna o histórico de transações da conta.

        Returns:
            str: O histórico das transações, armazenadas na pilha.

        Exemplos de uso:
            conta = Conta("12345")
            conta.depositar(500.0)
            historico = conta.exibeHistorico()
            print(historico)  # Histórico -> [Depósito: 500.0, Déposito inicial de: 0.0.]
        '''
        return self.historico.__str__()

    def __str__(self):
        '''
        Retorna uma representação em string da conta.

        Returns:
            str: Informação da conta, incluindo o número e saldo.

        Exemplos de uso:
            conta = Conta("12345", 1000.0)
            print(conta)  # "Conta 12345: Saldo 1000.0"

        '''
        return f'Conta {self.numero}: Saldo {self.saldo}'