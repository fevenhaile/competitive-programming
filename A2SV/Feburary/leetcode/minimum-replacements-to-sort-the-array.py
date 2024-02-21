class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count = 0
        i = len(nums)-2
        while i > -1:
            if nums[i+1] < nums[i]:
                amounts = math.ceil(nums[i]/nums[i+1])
                count += (amounts - 1)
                nums[i] = nums[i]//amounts
            i-=1
        return count
