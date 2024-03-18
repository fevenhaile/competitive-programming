class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = ([0] * (len(s)+1))

        for i in range(len(shifts)):
            if shifts[i][2] == 0:
                prefix[shifts[i][0]] -= 1 
                prefix[shifts[i][1]+1] += 1
                
            elif shifts[i][2] == 1:
                prefix[shifts[i][0]] += 1 
                prefix[shifts[i][1]+1] -= 1
               
        for i in range(1,len(prefix)-1):
            prefix[i] += prefix[i-1]
        prefix.pop() 
        print(prefix)

        ourl = list(s)
        print(ord(ourl[0]) + 1)

        for i in range(len(ourl)):
            ourl[i] = chr((ord(ourl[i]) - 97 + prefix[i]) % 26 + 97)
        return ''.join(ourl)

        # for i in range(len(ourl)):
        #     ord(ourl[i]) += prefix[i]
        
            


