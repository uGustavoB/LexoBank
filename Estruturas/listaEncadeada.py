class ListaError(Exception):
    def __init__(self, msg):
        super().__init__(msg)
 
class No:
    def __init__(self, carga):
        self.carga = carga
        self.proximo = None
    
    def __str__(self) -> str:
        return f"{self.carga}"
    
class Lista:
    def __init__(self):
        self.__head = None
        self.__tamanho = 0

    def __len__(self):
        return self.__tamanho
    
    def tamanho(self):
        return len(self)
    
    def estaVazia(self):
        return self.__head is None
    
    def elemento(self, posicao):
        if not (0 < posicao <= len(self)):
            raise ListaError(f"Posição inválida. Lista contém {self.__tamanho} elementos")
        
        cursor = self.__head
        for _ in range(posicao - 1):
            cursor = cursor.proximo
        return cursor.carga
    
    def busca(self, chave):
        cursor = self.__head
        contador = 1
        while cursor is not None:
            if chave == cursor.carga:
                return contador
            cursor = cursor.proximo
            contador += 1
        raise ListaError("Chave não encontrada na lista.")
    
    def modificar(self, posicao, carga):
        if not (0 < posicao <= len(self)):
            raise ListaError(f"Posição inválida. Lista contém {self.__tamanho} elementos")
        
        cursor = self.__head
        contador = 1
        while cursor is not None:
            if contador == posicao:
                cursor.carga = carga
                return
            cursor = cursor.proximo
            contador += 1

    # IMPLEMENTAÇÃO FUTURA - MOSTRAR DE FORMA ORGANIZADA O HISTORICO DE CADA CONTA CRIADA
    # VAI SER NECESSÁRIO CORRIGIR O SERVIDOR E CLIENTE, ENTÃO VAMOS MEDIR SE VALE A PENA FAZER ISSO KKK
    def adicionar_transacao(self, transacao): # INICIO
        self.inserir(len(self) + 1, transacao)
    
    def filtrar_por_conta(self, conta):
        cursor = self.__head
        resultado = []
        while cursor is not None:
            if f"conta {conta}" in cursor.carga:
                resultado.append(cursor.carga)
            cursor = cursor.proximo
        return resultado # FIM
    
    def inserir(self, posicao:int, carga:any):
        if not (0 < posicao <= len(self) + 1):
            raise ListaError(f"Posição inválida. Lista contém {self.__tamanho} elementos")

        if self.estaVazia():
            if posicao != 1:
                raise ListaError(f"A lista está vazia. A posição correta para inserção é 1.")
            self.__head = No(carga)
            self.__tamanho += 1
            return
        
        if posicao == 1:
            no = No(carga)
            no.proximo = self.__head
            self.__head = no
            self.__tamanho += 1
            return
        
        cursor = self.__head
        contador = 1
        while contador < posicao - 1:
            cursor = cursor.proximo
            contador += 1
        
        no = No(carga)
        no.proximo = cursor.proximo
        cursor.proximo = no
        self.__tamanho += 1

    def esvazia(self):
        while not self.estaVazia():
            self.remover(1)
    
    def remover(self, posicao):
        if not (0 < posicao <= len(self) + 1):
            raise ListaError(f"Posição inválida. Lista contém {self.__tamanho} elementos")

        if posicao == 1:
            carga = self.__head.carga
            self.__head = self.__head.proximo
            self.__tamanho -= 1
            return carga
        
        cursor = self.__head
        contador = 1
        while contador < posicao - 1:
            cursor = cursor.proximo
            contador += 1
        
        carga = cursor.proximo.carga
        cursor.proximo = cursor.proximo.proximo
        self.__tamanho -= 1
        return carga
        
    def __str__(self) -> str:
        mostrarLista = "Lista -> [ "

        cursor = self.__head
        while cursor is not None:
            mostrarLista += f"{cursor.carga}, "
            cursor = cursor.proximo
        
        mostrarLista = mostrarLista.strip(", ")
        mostrarLista += " ]"

        return mostrarLista