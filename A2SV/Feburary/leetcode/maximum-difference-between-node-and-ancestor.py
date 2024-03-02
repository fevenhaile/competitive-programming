# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def maxdif(root,minim,maxim):
            # base case
            if not root:
                return maxim - minim
            
            minim = min(minim,root.val)
            maxim = max(maxim,root.val)

            x = maxdif(root.left,minim,maxim)
            y = maxdif(root.right,minim,maxim)

            return max(x,y)
            
        return maxdif(root,root.val,root.val)