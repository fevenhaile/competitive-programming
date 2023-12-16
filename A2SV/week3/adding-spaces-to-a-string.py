class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces.append(len(s))
        temp_stack = []
        answer = []
        space_pointer = 0

        for i in range(len(s)):
            temp_stack.append(s[i])
            
            if spaces[space_pointer] == i:
                t = temp_stack.pop()
                answer.append("".join(temp_stack))
                temp_stack = [t]
                space_pointer += 1
        answer.append("".join(temp_stack))
        return " ".join(answer)
        
            
        
                


        