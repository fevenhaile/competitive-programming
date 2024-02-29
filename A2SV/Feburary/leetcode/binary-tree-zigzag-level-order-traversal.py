class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = {}
        ans = []

        def func(root, level):
            if not root:
                return
            dic.setdefault(level, []).append(root.val)
            func(root.left, level + 1)
            func(root.right, level + 1)

        func(root, 0)

        for i in dic:
            if i % 2 == 0:
                ans.append(dic[i])
            else:
                ans.append(dic[i][::-1])

        return ans