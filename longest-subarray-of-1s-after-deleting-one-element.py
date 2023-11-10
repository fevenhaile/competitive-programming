class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zerocounter = 0
        left = 0
        ans = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zerocounter += 1
            while zerocounter >= 2:
                if nums[left] == 0:
                    zerocounter -= 1
                left += 1
            ans = max(ans,right-left)
        return ans