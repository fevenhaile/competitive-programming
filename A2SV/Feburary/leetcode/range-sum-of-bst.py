# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sums = 0
        ans = []
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
        inorder(root)
        for i in range(len(ans)):
            if ans[i] <= high and ans[i] >= low:
                sums += ans[i]
        return sums

        