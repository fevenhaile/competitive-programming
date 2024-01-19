class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        x = 0
        
        for i in range(len(piles)//3,len(piles), 2):
            x += piles[i]
            
        return x

