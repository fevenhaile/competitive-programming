class Solution(object):
    def removeStars(self, s):
        stack=[]
        for i in s:
            if not stack or i!='*':
                stack.append(i)
            else:
                stack.pop()
        return "".join(stack)