class Solution:
    def splitArray(self, weights: List[int], k: int) -> int:
        def feasible(mid):
            count = 1
            curr_sums = 0
            for i in range(len(weights)):
                curr_sums += weights[i]
                if curr_sums > mid:
                    count += 1
                    curr_sums = weights[i]
            return count <= k
        
        low = max(weights)
        high  = sum(weights)
       
        while low <= high:
            mid = (low+high)//2
            if feasible(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low


