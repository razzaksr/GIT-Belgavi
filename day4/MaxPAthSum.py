from ConstructTree import Construction
from TreeNode import TreeNode
class Solution:
    def __init__(self):
        self.mSum = float('-inf')
    def findMax(self,node):
        if not node: return 0
        lmax = max(self.findMax(node.left),0)
        rMax = max(self.findMax(node.right),0)
        self.mSum = max(self.mSum,node.data+lmax+rMax)
        return node.data+max(lmax,rMax)
    def maxGain(self,root):
        self.findMax(root)
        return self.mSum
con = Construction();con.root = TreeNode(-10)
con.root.left = TreeNode(9)
con.root.right = TreeNode(20)
con.root.right.left = TreeNode(15)
con.root.right.right = TreeNode(7)
print(Solution().maxGain(con.root))