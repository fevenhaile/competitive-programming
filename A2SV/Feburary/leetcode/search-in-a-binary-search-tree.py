# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        # base case
        if not root:
            return root
        if root.val == val:
            return root
        # search for the val first
            
       
        if val > root.val:
            right = self.searchBST(root.right,val)
            return right
            
        elif val < root.val:
            left = self.searchBST(root.left,val)
            return left
           
        
        


        
        