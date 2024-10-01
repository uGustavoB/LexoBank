from conta import Conta
from Estruturas.avlTree import AVLTree

class GerenciadorContas:
    """
    Classe que gerencia as contas bancárias utilizando uma árvore AVL

    Atributos:
        __contas (AVLTree): Instância da estrutura de dados que é responsável por armazenas as contas bancárias.
    """
    def __init__(self):
        ''' Inicializa o gerenciador de contas com uma árvore AVL '''
        self.__contas = AVLTree()

    def criar_conta(self, numero:int, saldo:float) -> bool:
        '''
        Método que cria uma nova conta e adiciona à árvore de contas.

        Parâmetros:
            numero (int): O número da conta a ser criada
            saldo (float): O saldo inicial da conta

        Returns:
            tuple: Um código indicando o resultado da operação e uma mensagem opcional.
            Códigos:   
                - 201: Conta criada com sucesso.
                - 301: Conta já existe.
                - 305: Saldo inicial não pode ser negativo # (menor que 0).

        Exemplos de uso:
            gerenciador = GerenciadorContas()
            resultado = gerenciador.criar_conta(12345, 1000.0)
            print(resultado) # (201, None)
        '''
        if self.__contas.search(numero):
            return 301
        if saldo < 0:
            return 305
        
        conta = Conta(numero, saldo)
        self.__contas.insert(conta)  # Insere o objeto Conta na árvore AVL
        conta.historico.empilha(f"Déposito inicial de: {saldo}.")
        return 201

    def consultar_saldo(self, numero:int) -> float:
        '''
        Método que consulta o saldo de uma conta.

        Parâmetros:
            numero(int): O número da conta que o saldo será consultado.
        
        Returns:
            tuple: Um código e uma mensagem opcional com o saldo
                Códigos:
                - 200: Operação realizada com sucesso.
                - 300: Conta não encontrada.
        
        Exemplos de uso:
            saldo = gerenciador.consultar_saldo(12345)
            print(saldo) # (200, "Saldo: 1000.0")
        '''
        # Gustavo - Retornar o saldo da conta na tupla
        conta = self.__contas.search(numero)
        if conta:
            return (200, conta.saldo)
        return 300

    def depositar(self, numero:int, valor:float) -> bool:
        '''
        Método que deposita um valor na conta informada.

        Parâmetros:
            numero (int): O número da conta na qual o valor será depositado.
            valor (float): O valor a ser depositado.
        
        Returns:
            tumple: Um código e uma mensagem opcional.
                Códigos:
                - 200: Operação realizada com sucesso.
                - 300: Conta não encontrada.

        Exemplos de uso:
            resultado = gerenciador.depositar(12345, 500.0)
            print(resultado)
        '''
        conta = self.__contas.search(numero)
        if isinstance(conta, Conta):
            return conta.depositar(valor) 
        return 300
    
    def sacar(self, numero:int, valor:float) -> bool:
        '''
        Método que saca um valor da conta especificada.

        Parâmetros:
            numero (int): O número da conta que o valor será sacado.
            valor (float): O valor a ser sacado.

        Returns:
            tuple: Um código e uma mensagem opcional.
                Códigos:
                - 200: Operação realizada com sucesso.
                - 300: Conta não encontrada.

        Exemplos de uso:
            resultado = gerenciador.sacar(12345, 600.0)
            print(resultado) # (200, None)
        '''
        conta = self.__contas.search(numero)
        if isinstance(conta, Conta):
            return conta.sacar(valor) 
        return 300

    def transferir(self, numero_origem: str, numero_destino: str, valor: float) -> bool:
        '''
        Método que transfere um valor de uma conta para outra.

        Parâmetros:
            tuple: Um código e uma mensagem opcional.
                Códigos:
                - 200:Operação realizada com sucesso.
                - 303: Não é possível transferir para a mesma conta.
                - 300: Conta não encontrada.

        Exemplos de uso:
            resultado = gerenciador.transferir(12345, 67890, 200.0)
            print(resultado)  # (200, None)
        '''
        conta_origem = self.__contas.search(numero_origem)
        conta_destino = self.__contas.search(numero_destino)

        if conta_origem and conta_destino:
            if conta_origem.numero == conta_destino.numero:
                return 303

            resultado_saque = conta_origem.sacar(valor)
            if resultado_saque == 200: 
                conta_destino.depositar(valor)
                return 200

            return resultado_saque
        return 300

    def historico(self, numero:int) -> str:
        '''
        Método que retorna o histórico de transações de uma conta.

        Parâmetros:
            numero (int): O número da conta que o histórico será consultado.

        Returns:
            tuple: Um código e o histórico de transações ou None.
                Códigos: 
                - 200:Operação realizada com sucesso.
                - 300: Conta não encontrada.

        Exemplos de uso:
            resultado = gerenciador.historico(12345)
            print(resultado)  # (200, "Histórico -> [Déposito inicial de: 100.0.]")
        '''
        conta = self.__contas.search(numero)
        if conta:
            return (200, conta.exibeHistorico())
        return 300