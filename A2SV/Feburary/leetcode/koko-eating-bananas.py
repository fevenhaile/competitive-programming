class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(mid):
            count = 0
            curr_sums = 0
            for i in range(len(piles)):
                count += ceil(piles[i]/mid)
                if count > h:
                    return 0
            return True
            
        
        low = 1
        high  = sum(piles)
       
        while low <= high:
            mid = (low+high)//2
            if feasible(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low