class Solution:
    def nextGreaterElements(self, temperatures: List[int]) -> List[int]:
        # decreasing monotonic stack
        # have a visited
        # ans = [-1] * len(nums)
        # stack = []
        # visited = set()
        # for i in range(len(nums)):
        #     while stack and stack[-1] < nums[i]:
        #         ans[i] = nums[i]
        #         x = stack.pop()
        #         visited.add(x)
        #     if nums[i] not in visited:
        #         stack.append([nums[i]])
        # return ans
        stack = []
        ans = [-1] * len(temperatures)
        for i in range(len(temperatures)*2):
            i %= len(temperatures) 
            while stack and stack[-1][0] < temperatures[i]:
                x,ind = stack.pop()
                ans[ind] = temperatures[i]

            stack.append([temperatures[i],i])
        return ans 
            