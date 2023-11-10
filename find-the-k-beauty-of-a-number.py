class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        counter = 0
        for i in range(len(s)-k+1):
            x =  int(s[i:i+k])
            if x and num%x == 0:
                # print(x)
                counter += 1
        return counter