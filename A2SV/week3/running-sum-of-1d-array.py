class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        array = []
        x = 0
        for i in range(len(nums)):
            x += nums[i]
            array.append(x)
        return array
