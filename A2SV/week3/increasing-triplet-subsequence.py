class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest = float("inf")
        small = float("inf")
        
        for num in nums:
            if num <= smallest:
                smallest = num
            elif num <= small:
                small = num
            else:
                return True
        
        return False
        
            

        
            
          