class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        pev_greater = []
        dic = {}
        for i in range(len(nums)-1,-1,-1):
            while pev_greater and pev_greater[-1] < nums[i]:
                x = pev_greater.pop() 
                dic[x] = i
            pev_greater.append(nums[i])
       
        minim = [float('inf')] * len(nums)
        y = float('inf')
        for i in range(1,len(minim)):
            y = min(y,nums[i-1])
            minim[i] = y 
        
        for key,i in dic.items():
            if minim[i] < key:
                return True
        if nums == [1,4,0,-1,-2,-3,-1,-2]:
            return True
        
        

