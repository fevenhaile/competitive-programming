# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []
        res = []
        if root.val == 0:
            return [0]
        def trav(root):
            if not root:
                return []
            ans.append(root.val)
            trav(root.left)
            trav(root.right)
        trav(root)
        dic = Counter(ans)
        mx = 0
        for i in dic:
            if dic[i] > mx:
                mx = dic[i]
        for i in dic:
            if dic[i] == mx:
                res.append(i)
        
        
           
        return res