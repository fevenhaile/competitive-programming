class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                x,ind = stack.pop()
                ans[ind] = i - ind 

            stack.append([temperatures[i],i])
        return ans