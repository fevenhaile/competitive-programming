class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # closest to the target 
        # I wil have another array that I will put my sum of arrays 
        # jn to and check hich one is close by checking the difference
        
        minim = float('inf')
        nums.sort()
        
        
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l < r:
                sums = nums[i] + nums[l] +nums[r]
                if abs(target - sums) < abs(target - minim):
                    minim = sums
                if sums == target:
                    return sums
                elif sums < target:
                    l += 1
                else:
                    r -= 1
                
                
                
                
        return minim
            
            

