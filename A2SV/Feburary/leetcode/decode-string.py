class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        
        for i in range(len(s)):
            if not stack or s[i] != ']':
                stack.append(s[i])
            decoded = ''
            if s[i] == ']':
                while stack and stack[-1] != '[':
                    decoded = stack.pop() + decoded
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                stack.append(int(num) * decoded)
        return "".join(stack)
                 
                
            


            
        
        