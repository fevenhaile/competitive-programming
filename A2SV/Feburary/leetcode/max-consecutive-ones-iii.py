class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zerocounter = 0
        maxcount = 0 
        l = 0
        r = 0

        while r < len(nums):
            if nums[r] == 0:
                zerocounter += 1
            while zerocounter > k:
                if nums[l] == 0:
                    zerocounter -= 1
                l += 1
            r += 1
            maxcount = max(maxcount,r-l)
        return maxcount