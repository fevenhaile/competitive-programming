class Solution:
    def minimumSteps(self, s: str) -> int:
        right = 0
        ones = 0
        swaps = 0
        
        while right < len(s):
            if s[right] == "1":
                ones += 1
            else:
                swaps += ones
            right += 1

        return swaps

   

            
             