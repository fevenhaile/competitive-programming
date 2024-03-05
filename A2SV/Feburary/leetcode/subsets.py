class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        comb = []
        
        def backtrack(j):
            if len(comb) <= len(nums):
                ans.append(comb[:])
            
            for i in range(j,len(nums)):
                comb.append(nums[i])
                
                backtrack(i+1)
                comb.pop()
                
                            
        backtrack(0)
        return ans

            