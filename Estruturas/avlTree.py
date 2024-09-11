class Node:
    '''
    Classe que modela um nó dinâmico de uma árvore binária.
    '''
    def __init__(self, value: object):
        '''
        Construtor que inicializa um nó com um valor e sem filhos.
        '''
        self.__value = value
        self.__left = None
        self.__right = None
        self.__height = 1

    @property
    def value(self) -> object:
        return self.__value

    @value.setter
    def value(self, newValue: object):
        self.__value = newValue

    @property
    def left(self) -> 'Node':
        return self.__left

    @left.setter
    def left(self, newLeftChild: 'Node'):
        self.__left = newLeftChild

    @property
    def right(self) -> 'Node':
        return self.__right

    @right.setter
    def right(self, newRightChild: 'Node'):
        self.__right = newRightChild

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, newHeight: int):
        self.__height = newHeight

    def __str__(self):
        return f'|{self.__value.numero}:h={self.__height}|'

class AVLTree:
    '''
    Classe que cria uma árvore AVL em memória. A árvore AVL é uma Árvore Binária de Busca (BST) auto-balanceada,
    onde a diferença entre as alturas das subárvores esquerda e direita não pode ser maior que um para todos os nós.
    '''
    def __init__(self):
        self.__root = None

    def getRoot(self) -> any:
        return None if self.__root is None else self.__root.value

    def isEmpty(self) -> bool:
        return self.__root is None

    def search(self, key: str) -> 'Conta':
        node = self.__searchData(key, self.__root)
        return node.value if node is not None else None

    def __searchData(self, key: str, node: Node) -> Node:
        if node is None:
            return None
        if key == node.value.numero:
            return node
        elif key < node.value.numero:
            return self.__searchData(key, node.left)
        else:
            return self.__searchData(key, node.right)

    def insert(self, value: 'Conta'):
        if self.__root is None:
            self.__root = Node(value)
        else:
            self.__root = self.__insert(self.__root, value)

    def __insert(self, root: Node, value: 'Conta') -> Node:
        if root is None:
            return Node(value)
        elif value.numero < root.value.numero:
            root.left = self.__insert(root.left, value)
        else:
            root.right = self.__insert(root.right, value)

        root.height = 1 + max(self.__getHeight(root.left), self.__getHeight(root.right))

        balance = self.__getBalance(root)

        if balance > 1 and value.numero < root.left.value.numero:
            return self.__rightRotate(root)

        if balance < -1 and value.numero > root.right.value.numero:
            return self.__leftRotate(root)

        if balance > 1 and value.numero > root.left.value.numero:
            root.left = self.__leftRotate(root.left)
            return self.__rightRotate(root)

        if balance < -1 and value.numero < root.right.value.numero:
            root.right = self.__rightRotate(root.right)
            return self.__leftRotate(root)

        return root

    def __leftRotate(self, p: Node) -> Node:
        u = p.right
        T2 = u.left
        u.left = p
        p.right = T2
        p.height = 1 + max(self.__getHeight(p.left), self.__getHeight(p.right))
        u.height = 1 + max(self.__getHeight(u.left), self.__getHeight(u.right))
        return u

    def __rightRotate(self, p: Node) -> Node:
        u = p.left
        T2 = u.right
        u.right = p
        p.left = T2
        p.height = 1 + max(self.__getHeight(p.left), self.__getHeight(p.right))
        u.height = 1 + max(self.__getHeight(u.left), self.__getHeight(u.right))
        return u

    def __getHeight(self, node: Node) -> int:
        if node is None:
            return 0
        return node.height

    def __getBalance(self, node: Node) -> int:
        if node is None:
            return 0
        return self.__getHeight(node.left) - self.__getHeight(node.right)

    def delete(self, key: str):
        if self.__root is not None:
            self.__root = self.__delete(self.__root, key)

    def __delete(self, root: Node, key: str) -> Node:
        if root is None:
            return root
        elif key < root.value.numero:
            root.left = self.__delete(root.left, key)
        elif key > root.value.numero:
            root.right = self.__delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.__getMinValueNode(root.right)
            root.value = temp.value
            root.right = self.__delete(root.right, temp.value.numero)
        if root is None:
            return root
        root.height = 1 + max(self.__getHeight(root.left), self.__getHeight(root.right))
        balance = self.__getBalance(root)
        if balance > 1 and self.__getBalance(root.left) >= 0:
            return self.__rightRotate(root)
        if balance < -1 and self.__getBalance(root.right) <= 0:
            return self.__leftRotate(root)
        if balance > 1 and self.__getBalance(root.left) < 0:
            root.left = self.__leftRotate(root.left)
            return self.__rightRotate(root)
        if balance < -1 and self.__getBalance(root.right) > 0:
            root.right = self.__rightRotate(root.right)
            return self.__leftRotate(root)
        return root

    def __getMinValueNode(self, root: Node) -> Node:
        if root is None or root.left is None:
            return root
        return self.__getMinValueNode(root.left)

    def __getMaxValueNode(self, root: Node) -> Node:
        if root is None or root.right is None:
            return root
        return self.__getMaxValueNode(root.right)

    def __str__(self):
        return self.__strPreOrder(self.__root)

    def __strPreOrder(self, root: Node) -> str:
        if root is None:
            return ''
        else:
            return f'{root} {self.__strPreOrder(root.left)} {self.__strPreOrder(root.right)}'
