class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        sums = sum(nums)
        ones = sums
        zeroes = sums
        result  = [0]
        
        for L in range(len(nums)):
            if nums[L] == 0:
                zeroes += 1
            else:
                zeroes -= 1
            
            if zeroes == ones:
                result.append(L+1)
            elif zeroes > ones:
                ones = zeroes
                result = [L+1]
        return result 
                


        
        