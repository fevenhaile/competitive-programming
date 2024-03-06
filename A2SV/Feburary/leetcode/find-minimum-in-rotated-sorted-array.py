class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) -1
        ans = float('inf')
        while low <= high:
            mid  = (low + high)//2
            if nums[mid] > nums[high]:
                ans = min(ans,nums[mid])
                low = mid + 1
                
            else:
                ans = min(ans,nums[mid])
                high = mid - 1
                
        return ans
                