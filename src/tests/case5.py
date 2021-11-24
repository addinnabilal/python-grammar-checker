import sys
from time import time

class Node:
#     # Initialize the node with two child nodes, right node can be empty
    def __init__(self, sym, left, right):
        self.sym = sym
        self.left = left
        self.right = right