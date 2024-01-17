class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix = []
        x = 0
        for i in range(len(nums)):
            prefix.append(x)
            x += nums[i]
        prefix.append(sum(nums))
        print(prefix)
        for i in range(len(prefix)-1):
            if prefix[i] == prefix[-1] - prefix[i+1]:
                return i
        return -1
           