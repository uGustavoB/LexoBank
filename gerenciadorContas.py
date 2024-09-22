from conta import Conta
from Estruturas.avlTree import AVLTree
from excecoes import ContaInexistenteError

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
            return 301, None
        if saldo < 0:
            return 305, None
        
        conta = Conta(numero, saldo)
        self.__contas.insert(conta)  # Insere o objeto Conta na árvore AVL
        conta.historico.empilha(f"Déposito inicial de: {saldo}.")
        return 201, None

    def consultar_saldo(self, numero:int) -> float:
        '''
        Consulta o saldo de uma conta
        '''
        conta = self.__contas.search(numero)
        if conta:
            return (200, f"Saldo: {conta.saldo}")
        return 300, None

    def depositar(self, numero:int, valor:float) -> bool:
        '''
        Deposita um valor na conta informada
        '''
        conta = self.__contas.search(numero)
        if isinstance(conta, Conta):
            return conta.depositar(valor)  # Retorna o código e a mensagem do depósito
        return 300, None  # Conta não encontrada
    
    def sacar(self, numero:int, valor:float) -> bool:
        '''
        Saca um valor da conta especificada
        '''
        conta = self.__contas.search(numero)
        if isinstance(conta, Conta):
            return conta.sacar(valor)  # Retorna o código e a mensagem do saque
        return 300, None  # Conta não encontrada

    def transferir(self, numero_origem: str, numero_destino: str, valor: float) -> bool:
        '''
        Transfere um valor de uma conta para outra
        '''
        conta_origem = self.__contas.search(numero_origem)
        conta_destino = self.__contas.search(numero_destino)

        if conta_origem and conta_destino:
            if conta_origem.numero == conta_destino.numero:
                return 303, None  # Erro: não pode transferir para a mesma conta

            # Tenta realizar o saque na conta de origem
            resultado_saque = conta_origem.sacar(valor)
            if resultado_saque[0] == 200:  # Se o saque for bem-sucedido
                # Realiza o depósito na conta de destino
                conta_destino.depositar(valor)
                return 200, None  # Transferência realizada com sucesso

            return resultado_saque  # Retorna o erro do saque
        return 300, None  # Conta(s) não encontrada(s)

    def historico(self, numero:int) -> str:
        '''
        Retorna o histórico de transações de uma conta
        '''
        conta = self.__contas.search(numero)
        if conta:
            return (200, conta.exibeHistorico())
        return 300, None