class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        prefix = []
        x = 0
        ans = 0
        for i in range(len(nums)):
            x += nums[i]
            prefix.append(x)
        for i in range(len(prefix)):
            if prefix[i] % k in dic:
                ans += dic[prefix[i]%k]
            dic[prefix[i] % k] += 1

            
                
        return ans

        