from TreeNode import *
from collections import deque
class Construction:
    def __init__(self): self.root = None
    # Pre order traversal
    def __lshift__(self,node):
        if node:
            print(node.data,end = "->")
            self<<node.left
            self<<node.right
    # Building Binary Tree
    def build(self,items,index=0):
        if index>=len(items) or items[index] is None: 
            return None
        node = TreeNode(items[index])
        node.left = self.build(items,2*index+1)
        node.right = self.build(items,2*index+2)
        return node
    def __xor__(self,items):
        if not items: return
        return self.build(items)
    # Building Binary Search Tree
    def buildBst(self, node, value):
        if node is None: return TreeNode(value)
        if value < node.data:
            node.left = self.buildBst(node.left,value)
        else:
            node.right = self.buildBst(node.right,value)
        return node
    def __and__(self,items):
        for each in items: 
            return self.buildBst(self.root,each)
    # level order traversal
    def __eq__(self, node):
        if not node: return
        que = deque();que.append(node)
        while que:
            popped = que.popleft()
            print(popped.data,end=" ")
            if popped.left: que.append(popped.left)
            if popped.right: que.append(popped.right)
        print()
# con = Construction()
# con.root = con&[98,52,65,31,20]
# con==con.root
# con=.root = con^[45,92,36,28] # building Binary Tree
# con&[45,92,36,28] # building BST
# con<<con.root # pre order traversal