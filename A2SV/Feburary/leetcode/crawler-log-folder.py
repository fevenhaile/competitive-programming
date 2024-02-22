class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        count = 0
        for i in range(len(logs)):
            if not (logs[i] == './' or logs[i] == '../'):
                stack.append(logs[i])
                count += 1
            if logs[i] == '../':
                if stack:
                    stack.pop()
                    count -= 1

        return count
        

        