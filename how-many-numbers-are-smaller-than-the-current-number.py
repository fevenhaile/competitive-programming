from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        dictionary = {}
        sn = sorted(nums)

        for x in range(len(sn)):
            if sn[x] not in dictionary:
                dictionary[sn[x]] = x

        for i in nums:
            result.append(dictionary[i])

        return result