class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic = defaultdict(int)
        for i in range(len(nums)):
            dic[nums[i]] = i
        print(dic)
        for i,j in operations:
            ind = dic[i]
            nums[ind] = j
            dic[j] = ind
        return nums


        