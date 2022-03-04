"""
Unival tree

A unival tree (which stands for “universal value”) is a tree where all nodes have the same value.
Given the root to a binary tree, count the number of unival subtrees.


    	   (0) -> n1
	      /   \
  n2 <- (0)   (1) -> n3
              / \
      n4 <- (1) (1) -> n5
            / \   \
    n6 <- (1) (1) (1) -> n8
               ^
                \
                n7
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


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
