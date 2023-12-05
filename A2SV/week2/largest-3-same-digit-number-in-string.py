class Solution:
    def largestGoodInteger(self, num: str) -> str:
        k = 3
        maxarray = []
        
        for i in range(len(num)-k+1):
            array = num[i:i+k]
            if num[i] == num[i+1] == num[i+2]:
                maxarray .append(array) 
        
        maxarray = sorted(maxarray, reverse=True)
        return maxarray[0] if maxarray else ""