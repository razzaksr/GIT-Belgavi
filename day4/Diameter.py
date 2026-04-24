from ConstructTree import Construction
from TreeNode import TreeNode
class Solution:
    def __init__(self):
        self.mDiameter = 0
    def findDepth(self,node):
        if not node: return 0
        lDepth = self.findDepth(node.left)
        rDepth = self.findDepth(node.right)
        self.mDiameter = max(self.mDiameter,lDepth+rDepth)
        return 1+max(lDepth,rDepth)
    def diameterOfBinaryTree(self,root):
        self.findDepth(root)
        return self.mDiameter
con = Construction();con.root = TreeNode(3)
con.root.left = TreeNode(9)
con.root.right = TreeNode(20)
con.root.right.left = TreeNode(15)
con.root.right.right = TreeNode(7)
print(Solution().diameterOfBinaryTree(con.root))