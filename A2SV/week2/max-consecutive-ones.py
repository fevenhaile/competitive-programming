class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        dic = {1:0}
        ans = 0

        for i in nums:
            if i == 1:
                dic[1] += 1
                ans = max(ans,dic[1])
            else:
                dic[1] = 0
        return ans