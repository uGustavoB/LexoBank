class ListaError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class No:
    def __init__(self, carga):
        '''
        Construtor que inicializa um nó com uma carga e nenhum próximo nó.
        '''
        self.carga = carga
        self.proximo = None

    def __str__(self) -> str:
        return f"{self.carga}"

class Lista:
    def __init__(self):
        '''
        Construtor que inicializa uma lista vazia.
        '''
        self.cabeca = None

    def esta_vazia(self) -> bool:
        '''
        Verifica se a lista está vazia.
        '''
        return self.cabeca is None

    def inserir(self, carga) -> None:
        '''
        Insere um elemento no início da lista.
        '''
        novo_no = No(carga)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no

    def remover(self, carga) -> None:
        '''
        Remove um elemento da lista.
        '''
        if self.esta_vazia():
            raise ListaError("A lista está vazia")
        
        atual = self.cabeca
        anterior = None
        while atual is not None:
            if atual.carga == carga:
                if anterior is None:
                    self.cabeca = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                return
            anterior = atual
            atual = atual.proximo
        raise ListaError(f"Elemento {carga} não encontrado")
    
    def imprimir(self) -> str:
        '''
        Retorna uma string que representa a lista.
        '''
        if self.esta_vazia():
            return "Lista vazia"
        return " -> ".join(str(item) for item in self)

    def __iter__(self):
        '''
        Permite iteração sobre a lista.
        '''
        atual = self.cabeca
        while atual is not None:
            yield atual.carga
            atual = atual.proximo

    def __str__(self) -> str:
        '''
        Retorna uma string que representa a lista.
        '''
        if self.esta_vazia():
            return "Lista vazia"
        return " -> ".join(str(item) for item in self)

    def __len__(self) -> int:
        '''
        Retorna o número de elementos na lista.
        '''
        return sum(1 for _ in self)

    def buscar(self, carga) -> bool:
        '''
        Verifica se um elemento está na lista.
        '''
        return carga in self
