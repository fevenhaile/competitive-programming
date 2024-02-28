# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def pretrav(root):
            if not root:
                return 
            arr.append(root.val)
            pretrav(root.left)
            pretrav(root.right)
        pretrav(root)
        return arr

        