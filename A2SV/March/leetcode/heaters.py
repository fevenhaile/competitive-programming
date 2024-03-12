class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def heat(mid):
            r = 0
            for l in range(len(houses)):
                while r < len(heaters) and abs(houses[l] - heaters[r]) > mid:
                    r += 1
                if r >= len(heaters):
                    return False
            return True
        
        low = 0
        high = max(houses) + max(heaters)

        while low <= high:
            mid = (low + high)//2
            if heat(mid):
                high = mid - 1
            else:
                low = mid + 1
        
        return low
                