class Solution:
    def maxScore(self, s: str) -> int:
        onecounter = 0
        zerocounter = 0
        maxim = float('-inf')
        
        for i in range(len(s)):
            if s[i] == "1":
                onecounter += 1
        
        for i in range(len(s) - 1):  
            if s[i] == "0":
                zerocounter += 1
            else:
                onecounter -= 1
            maxim = max(maxim, zerocounter + onecounter)
        
        return maxim