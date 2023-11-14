class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        xor=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(nums[i]-nums[j])<=min(nums[i],nums[j]):
                  xor.append(nums[i]^nums[j])
        return max(xor)