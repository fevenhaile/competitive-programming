# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = []
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
        inorder(root)
        print(ans)
        _sorted = sorted(ans)
        for i in range(len(ans)-1):
            if ans[i] == ans[i+1]:
                return False
        if _sorted == ans:
            return True
        
        
        