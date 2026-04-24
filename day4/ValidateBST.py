from ConstructTree import Construction
from TreeNode import TreeNode
class Solution:
    def validating(self,node,mn=float('-inf'),mx=float('inf')):
        if not node: return True
        if not (mn<node.data<mx): return False
        return (self.validating(node.left,mn,node.data)
                and
                self.validating(node.right,node.data,mx))
    def isValidBST(self,root):
        return self.validating(root)
sol = Solution()
con=Construction()
con.root = TreeNode(10)
con.root.left = TreeNode(6)
con.root.right = TreeNode(12)
con.root.left.left = TreeNode(9)
con.root.right.right = TreeNode(20)
print(sol.isValidBST(con.root))