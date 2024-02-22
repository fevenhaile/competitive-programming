class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            
            if tokens[i] != '+' and tokens[i] != '-' and tokens[i] != '*' and tokens[i] != '/':
                stack.append(int(tokens[i]))
            elif tokens[i] == '+' :
                
                x = stack.pop()
                y = stack.pop()
                stack.append(y+x)
            
            elif tokens[i] == '-':
                x = stack.pop()
                y = stack.pop()
                stack.append(y-x)
            elif tokens[i] == '*':
                x = stack.pop()
                y = stack.pop()
                stack.append(y*x)
            elif tokens[i] == '/':
                x = stack.pop()
                y = stack.pop()
                if y/x > 0:
                    stack.append(math.floor(y/x))
                else:
                    stack.append(math.ceil(y/x))
        return stack[0]





        