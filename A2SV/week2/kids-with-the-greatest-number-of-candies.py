class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        booleans=[]
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max(candies):
                booleans.append(True)
            else:
                booleans.append(False)
        return booleans
        