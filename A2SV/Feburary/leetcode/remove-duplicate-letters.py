class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dic = Counter(s)
        visited = set()
        stack = []
        for i in range(len(s)):
            while stack and stack[-1] > s[i] and dic[stack[-1]] > 1 and s[i] not in visited:
                x = stack.pop()
                visited.remove(x)
                dic[x] -= 1
            if s[i] not in visited:
                stack.append(s[i])
                visited.add(s[i])
            else:
                dic[s[i]] -= 1
                
        return ''.join(stack)