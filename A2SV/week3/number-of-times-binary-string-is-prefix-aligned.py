class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count  = 0
        max_idx = 0
        for i,value in enumerate(flips):
           max_idx = max(max_idx,value)
           if max_idx == i+1:
               count +=1 
        return count 
        
        
     