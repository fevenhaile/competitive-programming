# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # create a new node that stores the new values
        new_node = TreeNode()

        # define the bases cases
        if not root1 and root2:
            return root2
        if root1 and not root2:
            return root1
        if not root1 and not root2:
            return
        if root1 and root2:
            new_node.val = root1.val + root2.val

        
        #traverse through the two nodes at the same time
        new_node.left = self.mergeTrees(root1.left,root2.left)
        new_node.right = self.mergeTrees(root1.right,root2.right)

        return new_node

       
    
        



        
        
        
        
        
        
        
        
        
