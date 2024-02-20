class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        step = 0
        current = 1
        for i in range(n):
            current = max(current-1,nums[i])
            if i != n-1 and current == 0:
                return False
        return True
           
            


       



           
        

            



        