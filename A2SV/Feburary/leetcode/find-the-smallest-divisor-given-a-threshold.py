class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def feasible(mid):
            count = 0
            curr_sums = 0
            for i in range(len(nums)):
                count += ceil(nums[i]/mid)
                if count > threshold:
                    return 0
            return True
            
        
        low = 1
        high  = sum(nums)
       
        while low <= high:
            mid = (low+high)//2
            if feasible(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low