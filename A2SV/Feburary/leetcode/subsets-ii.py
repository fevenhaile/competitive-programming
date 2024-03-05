class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        sub = []
        nums.sort()

        # j keeps track of my index
        def backtrack(j):
            if len(sub) <= len(nums):
                ans.append(sub[:])
            
            for i in range(j,len(nums)):
                sub.append(nums[i])
                backtrack(i+1)
                sub.pop()
        backtrack(0)
        visited = []
        for i in range(len(ans)):
            if ans[i] not in visited:
                visited.append(ans[i])
            


        return visited
            
