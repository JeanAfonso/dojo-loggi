"""
Unival tree

A unival tree (which stands for “universal value”) is a tree where all nodes have the same value.
Given the root to a binary tree, count the number of unival subtrees.


    	   (0) -> n1        ------------------ nivel 0
	      /   \
  n2 <- (0)   (1) -> n3     ------------------ nivel 1
              / \
      n4 <- (1) (1) -> n5   ------------------ nivel 2
            / \   \
    n6 <- (1) (1) (1) -> n8 ------------------ nivel 3
               ^
                \
                n7
"""


# DFS -> depth first search (busca em profundidade): recursão/iterativa (lista)
# BFS -> breadth first search (busca em largura): iterativa (lista)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def dfs(self, callback):
        callback(self)

        if self.left:
            self.left.dfs(callback)
        if self.right:
            self.right.dfs(callback)

    def unival(self):
        right_all_true = left_all_true = True

        if self.left:
            left_all_true = self.value == self.left.value and self.left.unival()
        if self.right:
            right_all_true = self.value == self.right.value and self.right.unival()

        return right_all_true and left_all_true


"""
Passos:
- Acessa nó raíz
- Tenta acessar filho a esquerda, caso não, volta pro anterior
    - Se tem, entra no filho e ele vira o "raíz"
    - Volta ao passo 1
- Tenta acessar filho a direita, caso não, volta pro anterior
    - Se tem, entra no filho e ele vira o "raíz"
    - Volta ao passo 1
"""

n1 = Node(0)
n2 = Node(0)
n3 = Node(1)
n4 = Node(1)
n5 = Node(1)
n6 = Node(1)
n7 = Node(1)
n8 = Node(1)

n1.left = n2
n1.right = n3

n2.parent = n1

n3.parent = n1
n3.left = n4
n3.right = n5

n4.parent = n3
n4.left = n6
n4.right = n7

n5.parent = n3
n5.right = n8

n6.parent = n4

n7.parent = n4

n8.parent = n5

n1.unival()


count = 0


def count_univals(node: Node):
    if node.unival():
        global count
        count += 1


n1.dfs(count_univals)
print(count)

n1.dfs(lambda node: print(node.value))
