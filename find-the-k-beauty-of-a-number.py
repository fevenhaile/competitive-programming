class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s=str(num)
        counter=0
        
        for i in range(len(s)-k+1):
            casted=int(s[i:i+k])
            if casted and num % casted == 0:
                counter+=1
        return counter