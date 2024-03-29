class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = [1]
        if rowIndex == 0:
            return prev
        # building the thing 
        for i in range(1,rowIndex + 1):
            curr = [0] * (i+1)
            curr[0] = 1
            curr[-1] = 1
            
           
            for j in range(1,len(curr)-1):
                curr[j] = prev[j] + prev[j-1]
            prev = curr
        
        return curr
        

        