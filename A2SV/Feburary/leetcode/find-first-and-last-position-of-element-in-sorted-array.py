class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) -1
        res = []

        if target not in nums:
            return [-1,-1]

        # to find the first occurence
        while low <= high:
            mid = (low+high)//2
            if nums[mid] >= target:
                ans = mid
                high = mid - 1
                
            else:
                low  = mid + 1
        res.append(low)
        low = 0
        high = len(nums) -1    
        while low <= high:
            mid = (low+high)//2
            if nums[mid] <= target:
                low  = mid + 1
                
            else:
                high = mid - 1
        res.append(high)  
        
        return res
            
            