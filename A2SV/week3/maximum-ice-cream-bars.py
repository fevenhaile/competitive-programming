class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        x = 0
        
        if sum(costs) < coins:
            return len(costs)

        for i in range(len(costs)):
            x += costs[i]
            if x > coins:
                return i

        