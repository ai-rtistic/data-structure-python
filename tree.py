# 트리(Tree)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)
    

class Tree:
    def __init__(self):
        self.root = None   # root: 최상위노드 


# 트리 순회

def preorderTraversal(self, node):   # 전위 순회
    print(node, end='')   # 노드 방문
    if node.left is not None:   # 왼쪽 서브 트리 순회
        self.preorderTraversal(node.left)
    if node.right is not None:   # 오른쪽 서브트리 순회
        self.preorderTraversal(node.right)


def inorderTraversal(self, node):   # 중위 순회
    if node.left is not None:
        self.inorderTraversal(node.left)
    print(node, end='')
    if node.right is not None:
        self.inorderTraversal(node.right)

def postorderTraversal(self, node):   # 후위 순회
    if node.left is not None:
        self.postorderTraversal(node.left)
    if node.right is not None:
        self.postorderTraversal(node.right)
    print(node, end='')



# 이진 탐색 트리

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insertElement(self, data):   # 데이터 삽입
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
        
        node = self.root
        while True:
            pre_node = node
            if node.data > new_node.data:
                node = node.left
                if node == None:
                    node = new_node
                    pre_node.left = node
            elif node.data < new_node.data:
                node = node.right
                if node == None:
                    node = new_node
                    pre_node.right = node
            else: return


    def searchElement(self, data):  # 데이터 검색
        node = self.root
        while True:
            if node.data > data:
                node = node.left
            elif node.data < data:
                node = node.right
            elif node.data == data:
                break
            else:
                return Node('탐색 결과 없음')
        return node

    def preorderTraversal(self, node):   # 전위 순회
        print(node, end='')   # 노드 방문
        if node.left is not None:   # 왼쪽 서브 트리 순회
            self.preorderTraversal(node.left)
        if node.right is not None:   # 오른쪽 서브트리 순회
            self.preorderTraversal(node.right)


    def inorderTraversal(self, node):   # 중위 순회
        if node.left is not None:
            self.inorderTraversal(node.left)
        print(node, end='')
        if node.right is not None:
            self.inorderTraversal(node.right)

    def postorderTraversal(self, node):   # 후위 순회
        if node.left is not None:
            self.postorderTraversal(node.left)
        if node.right is not None:
            self.postorderTraversal(node.right)
        print(node, end='')