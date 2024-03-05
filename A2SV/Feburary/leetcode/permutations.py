class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        # base case
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            removed = nums.pop(0)
            per = self.permute(nums)

            for j in per:
                j.append(removed)
            ans.extend(per)
            nums.append(removed)
        return ans
