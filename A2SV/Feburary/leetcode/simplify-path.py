class Solution:
    def simplifyPath(self, path: str) -> str:
        # stack = []
        inbetween = path.split("/")
        stack = []
        ans = ''
        for i in inbetween:
            if i and i != '..' and i != '.' :
                stack.append(i)
            elif len(stack) != 0 and i == '..':
                stack.pop()
        for i in range(len(stack)):
            ans += '/' + stack[i] 
        if len(stack) == 0:
            ans  = '/'
        return ans



                        
        
        

        