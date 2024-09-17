from conta import Conta
from Estruturas.avlTree import AVLTree

class GerenciadorContas:
    def __init__(self):
        '''
        Inicializa o gerenciador de contas com uma árvore AVL
        '''
        self.__contas = AVLTree()

    def criar_conta(self, numero:int, saldo:float) -> bool:
        '''
        Cria uma nova conta e adiciona à árvore de contas
        '''
        if self.__contas.search(numero):
            raise ValueError("Conta já existe")
        if saldo < 0:
            raise ValueError("Saldo inicial não pode ser negativo")
        
        conta = Conta(numero, saldo)
        self.__contas.insert(conta)  # Insere o objeto Conta na árvore AVL
        conta.historico.empilha(f"Déposito inicial de: {saldo}.")
        return True

    def consultar_saldo(self, numero:int) -> float:
        '''
        Consulta o saldo de uma conta
        '''
        conta = self.__contas.search(numero)
        if conta:
            return conta.saldo
        raise ValueError("Conta não encontrada")

    def depositar(self, numero:int, valor:float) -> bool:
        '''
        Deposita um valor na conta informada
        '''
        conta = self.__contas.search(numero)
        if isinstance(conta, Conta):
            conta.depositar(valor)
            return True
        raise ValueError("Conta não encontrada")
    
    def sacar(self, numero:int, valor:float) -> bool:
        '''
        Saca um valor da conta especificada
        '''
        conta = self.__contas.search(numero)
        if isinstance(conta, Conta):
            conta.sacar(valor)
            return True
        raise ValueError("Conta não encontrada")

    def transferir(self, numero_origem: str, numero_destino: str, valor: float) -> bool:
        '''
        Transfere um valor de uma conta para outra
        '''
        conta_origem = self.__contas.search(numero_origem)
        conta_destino = self.__contas.search(numero_destino)
        
        if conta_origem and conta_destino:
            conta_origem.transferir(valor, conta_destino)
            return True
        raise ValueError("Conta não encontrada")

    def historico(self, numero:int) -> str:
        '''
        Retorna o histórico de transações de uma conta
        '''
        conta = self.__contas.search(numero)
        if conta:
            return conta.exibeHistorico()
        raise ValueError("Conta não encontrada")