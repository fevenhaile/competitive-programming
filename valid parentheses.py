class Solution(object):
    def isValid(self, s):
        stack=[]
        for bracket in s:
            if bracket in {"(","[","{"}:
                stack.append(bracket)
            else:
                if len(stack)==0:
                    return False
                popped=stack.pop()
                if(bracket==")" and popped!="(") or (bracket=="}" and popped!="{") or(bracket=="]" and popped!="["):
                    return False
        return (len(stack)==0)  
