from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        d = {}
        S = sorted(nums)
        #for each key we are giving a value here
        for x in range(len(S)):
            if S[x] not in d:
                d[S[x]] = x #in our dictionary the keys are the(values ofsortednums S)and the  values are their index

        for i in nums:
            result.append(d[i])

        return result