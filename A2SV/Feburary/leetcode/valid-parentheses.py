class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
            elif stack[-1] == '(' and s[i] == ")" or stack[-1] == '[' and s[i] == "]" or stack[-1] == '{' and s[i] == "}":
                stack.pop()
            else:
                stack.append(s[i])
        if len(stack) == 0:
            return True

        