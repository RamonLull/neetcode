# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def helper(root):
            if not root:
                return 0
            tmp = self.get_height(root.left) + self.get_height(root.right)
            self.ans = max(self.ans, tmp)
            helper(root.left)
            helper(root.right)
        helper(root)
        return self.ans

    def get_height(self, node):
        if not node:
            return 0
        left = self.get_height(node.left)
        right = self.get_height(node.right)
        return 1 + max(left, right)