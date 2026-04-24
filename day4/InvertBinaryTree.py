from ConstructTree import Construction
from TreeNode import TreeNode
def invert(root):
    if not root: return None
    root.left, root.right = root.right, root.left
    invert(root.left)
    invert(root.right)
    return root
con = Construction();con.root = TreeNode(4)
con.root.left = TreeNode(2)
con.root.right = TreeNode(7)
con.root.left.left = TreeNode(1)
con.root.left.right = TreeNode(3)
con.root.right.left = TreeNode(6)
con.root.right.right = TreeNode(9)
con==con.root
invertedRoot = invert(con.root)
con==invertedRoot
