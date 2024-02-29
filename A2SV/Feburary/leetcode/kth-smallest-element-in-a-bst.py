# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # traverse inorder to get increasing order
        ans = []
        dic = defaultdict()
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
        inorder(root)
        
        for i in range(len(ans)):
            dic[i] = ans[i] 
        return dic[k-1]
        
            
        