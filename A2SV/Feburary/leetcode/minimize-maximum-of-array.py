class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        prefix = []
        ans = 0
        minim = nums[0]
        for i in range(len(nums)):
            ans += nums[i]
            prefix.append(ans)
        for i in range(len(prefix)):
            if nums[i] > minim:
                minim = max(minim,ceil(prefix[i]/(i+1)))
        return minim

        