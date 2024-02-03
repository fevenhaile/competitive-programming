class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        #  just focus on finding the first subarray that contains the subarray
        sets = set(nums)
        l= 0
        subarray = 0
        dic = defaultdict()

        for r in range(len(nums)):
            if nums[r] in dic:
                dic[nums[r]] += 1
            else:
                dic[nums[r]] = 1
            while l < len(nums)and r<len(nums)and len(sets) == len(dic):
                subarray += len(nums) - r
                dic[nums[l]]-=1
                if dic[nums[l]] == 0:
                    del dic[nums[l]]
                l += 1
                print(dic)
                
                

        return subarray
            