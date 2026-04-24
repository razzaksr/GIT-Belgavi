from ConstructTree import Construction
from TreeNode import TreeNode
class Solution:
    def isLeaf(self,node):
        return node and not node.left and not node.right
    def sumOfLeftLeaves(self,root):
        if not root: return 0
        sum = 0;
        if self.isLeaf(root.left): sum += root.left.data
        else: sum += self.sumOfLeftLeaves(root.left)
        sum += self.sumOfLeftLeaves(root.right)
        return sum
con = Construction();con.root = TreeNode(3)
con.root.left = TreeNode(9)
con.root.right = TreeNode(20)
con.root.right.left = TreeNode(15)
con.root.right.right = TreeNode(7)
print(Solution().sumOfLeftLeaves(con.root))
