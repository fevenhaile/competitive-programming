class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n  = len(nums)
        
        freq  = [0] * (n+1)
        for i in range(len(requests)):
            freq[requests[i][0]] += 1
            freq[requests[i][1] + 1] -=1
        x = 0
        for i in range(len(freq)):
            x += freq[i]
            freq[i] = x
        freq.pop
        freq.sort(reverse = True)
        print(freq)

        nums.sort(reverse =True)
        total = 0
        for i in range(len(nums)):
            total += nums[i] *freq[i]
        return total % (10**9 + 7)

        

        


        


