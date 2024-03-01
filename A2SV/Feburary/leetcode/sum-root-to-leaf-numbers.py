# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # how to know if it is a leaf node\\
        self.ans = []
        path = []
        def trav(root,path):
        
            if not root:
                return
            if not root.left and not root.right:
                path.append(root.val)
                self.ans.append(int(''.join(str(i) for i in path)))
                print(path)
                return 
            path.append(root.val)
            trav(root.left,path[::])
            trav(root.right,path[::])
        trav(root,[])
        print(self.ans)
        return sum(self.ans)
            

        
       

        
        