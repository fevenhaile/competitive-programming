class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n =len(grid)
        ans = 0
        _zip = list(zip(*grid))
        for i in range(len(grid)):
            for j in range(len(_zip)):
                m1 = max(grid[i][:n])
                m2 = max(_zip[j][:n])
                ans += min(m1,m2) - grid[i][j]
        return ans

      
        
