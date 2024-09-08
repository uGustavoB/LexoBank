class Node:
    '''
    Class that models a dinamic node of a binary tree.
    '''
    def __init__(self,value:object):
        '''
        Constructor that initializes a node with a data and
        without children.'''
        self.__value = value
        self.__left = None
        self.__right = None
        # attribute that specifies the height (balance factor of the node)
        self.__height = 1

    @property
    def value(self)->object:
        return self.__value

    @value.setter
    def value(self, newValue:object):
        self.__value = newValue

    @property
    def left(self)->'Node':
        return self.__left

    @left.setter
    def left(self, newLeftChild:object):
        self.__left = newLeftChild

    @property
    def right(self)->'Node':
        return self.__right

    @right.setter
    def right(self, newRightChild:'Node'):
        self.__right = newRightChild

    @property
    def height(self)->int:
        return self.__height

    @height.setter
    def height(self, newHeight:int):
        self.__height = newHeight

    def insertLeft(self, data:object):
        if self.__left == None:
            self.__left = Node(data)	

    def hasLeftChild(self)->bool:
        return self.__left != None

    def hasRightChild(self)->bool:
        return self.__right != None

    def insertRight(self,data:object):
        if self.__right == None:
            self.__right = Node(data)

    def __str__(self):
        return f'|{self.__value}:h={self.__height}|'
    

# Classe AVL tree 
class AVLTree(object): 
    """ 
    Class that creates a AVL tree in memory. AVL tree is a self-balancing
    Binary Search Tree (BST) where the difference between heights
    of left and right subtrees cannot be more than one for all nodes. 
    """
    def __init__(self, value:object = None):
        self.__root = None if value is None else self.insert(value)

    def getRoot(self)->any:
        return None if self.__root is None else self.__root.value

    def isEmpty(self)->bool:
        return self.__root == None

    def search(self, key:any )->any:
        if self.__root != None:
           node = self.__searchData(key, self.__root)
           return node.value if node is not None else None
        else:
            return None
    
    def __searchData(self, key:any, node:Node)->Node:
        if key == node.value:
            return node
        elif key < node.value and node.left != None:
            return self.__searchData(key, node.left())
        elif key > node.value and node.right != None:
            return self.__searchData(key, node.right)
        else:
            return None

    def __len__(self)->int:
        return self.__count(self.__root)

    def __count(self, node:Node)->int:
        if node == None:
            return 0
        else:
            return 1 + self.__count(node.left) + self.__count(node.right)

    def insert(self, key:object):
        if self.__root == None:
            self.__root = Node(key)
        else:
            self.__root = self.__insert(self.__root, key)
  
    def __insert(self, root:Node, key:any):
        if not root: 
            return Node(key) 
        elif key < root.value: 
            root.left = self.__insert(root.left, key) 
        else: 
            root.right = self.__insert(root.right, key) 
  
        root.height = 1 + max(self.__getHeight(root.left), 
                              self.__getHeight(root.right)) 
  
        balance = self.__getBalance(root) 
  
        if balance > 1 and key < root.left.value: 
            return self.__rightRotate(root) 
  
        if balance < -1 and key > root.right.value: 
            return self.__leftRotate(root) 
  
        if balance > 1 and key > root.left.value: 
            root.left = self.__leftRotate(root.left) 
            return self.__rightRotate(root) 
  
        if balance < -1 and key < root.right.value: 
            root.right = self.__rightRotate(root.right) 
            return self.__leftRotate(root) 
  
        return root 
  
    def __leftRotate(self, p:Node)->Node: 
        u = p.right 
        T2 = u.left 
        u.left = p 
        p.right = T2 
        p.height = 1 + max(self.__getHeight(p.left), 
                         self.__getHeight(p.right)) 
        u.height = 1 + max(self.__getHeight(u.left), 
                         self.__getHeight(u.right)) 
        return u 
  
    def __rightRotate(self, p:Node)->Node: 
        u = p.left 
        T2 = u.right 
        u.right = p 
        p.left = T2 
        p.height = 1 + max(self.__getHeight(p.left), 
                        self.__getHeight(p.right)) 
        u.height = 1 + max(self.__getHeight(u.left), 
                        self.__getHeight(u.right)) 
        return u 
  
    def __getHeight(self, node:Node)->int: 
        if node is None: 
            return 0
        return node.height 
  
    def __getBalance(self, node:Node)->int: 
        if not node: 
            return 0
        return self.__getHeight(node.left) - self.__getHeight(node.right)

    def __getMinValueNode(self, root:Node)->Node:
        if root is None or root.left is None:
            return root
        return self.__getMinValueNode(root.left)
    
    def __getMaxValueNode(self, root:Node)->Node:
        if root is None or root.right is None:
            return root
        return self.__getMaxValueNode(root.right)  
    
    def preorder(self):
        self.__preorder(self.__root)

    def __preorder(self, root): 
        if not root: 
            return
        print("{0} ".format(root.value), end="") 
        self.__preorder(root.left) 
        self.__preorder(root.right) 

    def inorder(self):
        self.__inorder(self.__root)

    def __inorder(self, root): 
        if not root: 
            return
        self.__inorder(root.left) 
        print("{0} ".format(root.value), end="") 
        self.__inorder(root.right) 

    def posorder(self):
        self.__posorder(self.__root)

    def __posorder(self, root): 
        if not root: 
            return
        self.__posorder(root.left) 
        self.__posorder(root.right) 
        print("{0} ".format(root.value), end="") 

    def delete(self, key:object):
        if self.__root is not None:
            self.__root = self.__delete(self.__root, key)
        

    def __delete(self, root:Node, key:object)->Node: 
        if not root: 
            return root   
        elif key < root.value: 
            root.left = self.__delete(root.left, key)   
        elif key > root.value: 
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
            root.right = self.__delete(root.right, temp.value) 
        if root is None: 
            return root 
        root.height = 1 + max(self.__getHeight(root.left), 
                            self.__getHeight(root.right)) 
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
    
    def __str__(self):
        return self.__strPreOrder(self.__root)
    
    def __strPreOrder(self, root:Node)->str:
        if root is None:
            return ''
        else:
            return f'{root} {self.__strPreOrder(root.left)} {self.__strPreOrder(root.right)}'