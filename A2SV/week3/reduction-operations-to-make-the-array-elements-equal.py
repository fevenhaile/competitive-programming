class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
       
        count = 0
        dic = defaultdict()
        x = list(set(nums))
        x.sort()
        for key,value in enumerate(x):
            dic[value] = key
        print(dic)
        for i in range(len(nums)):
            count += dic[nums[i]]
        return count
        



         
            

        
        