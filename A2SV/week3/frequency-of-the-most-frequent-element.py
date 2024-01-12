class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = 0
        maxim = 1
        sums = 0
        while r < len(nums):
            sums += nums[r]
            if (nums[r] * (r - l + 1)) - sums <= k:
                maxim = max(maxim, r - l + 1)
                
            else:
                while (nums[r] * (r - l + 1)) - sums > k and l < r:
                    sums -= nums[l]
                    l += 1
            r += 1
        return maxim