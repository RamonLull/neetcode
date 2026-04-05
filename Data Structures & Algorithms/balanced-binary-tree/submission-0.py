# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.max_diff = 0
        def height(root):
            if not root:
                return 0
            left_height = height(root.left)
            right_height = height(root.right)
            self.max_diff = max(self.max_diff, abs(left_height - right_height))
            return 1 + max(left_height, right_height)
        height(root)
        return self.max_diff <= 1