class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        frequency = []

        for i in range(0, len(nums), 2):
            frequency.extend([nums[i+1]] * nums[i])

        return frequency