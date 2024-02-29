# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # write a function
        def issame(left,right):
            # base case
            if not left and not right:
                return True
            if not left and right:
                return False
            if not right and left:
                return False
            if left.val != right.val:
                return False
            if issame(left.left,right.left) and issame(left.right,right.right):
                return True
            return False
            # if issame(left,right.left) == issame(left.left,right):
            #     return True
         
        return issame(p,q)


        