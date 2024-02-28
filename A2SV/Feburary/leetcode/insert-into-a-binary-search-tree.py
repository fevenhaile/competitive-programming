# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]: 
        # ayios ayios ayios ayios ayios 
        # temp = root.val
        # root.val = temp
        # TreeNode = []

        def binarysearch(root,val):
            if not root:
                return TreeNode(val)

            if val > root.val:
                root.right = binarysearch(root.right,val)
                return root
                
                

            else:
                root.left = binarysearch(root.left,val)
                return root
                
                
                
                
        return binarysearch(root,val)
        # return root


         
    
