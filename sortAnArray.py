class Solution(object):
    def sortArray(self, nums):
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        
        left = self.sortArray(left)
        right = self.sortArray(right)
        
        return self.merge(left, right)
    
    def merge(self, left, right):
        merged = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        
        while i < len(left):
            merged.append(left[i])
            i += 1
        
        while j < len(right):
            merged.append(right[j])
            j += 1
        
        return merged
        