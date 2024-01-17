class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap={0:1}
        s=count=0
        for i in range(len(nums)):
            s+=nums[i]
            if s-k in hashmap:
                count+=hashmap[s-k]
            if s in hashmap:
                hashmap[s]+=1
            else:
                hashmap[s]=1
        return count