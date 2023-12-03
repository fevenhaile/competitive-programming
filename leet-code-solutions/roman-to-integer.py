class Solution:
    def romanToInt(self, s: str) -> int:
        r = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        v = [1, 5, 10, 50, 100, 500, 1000]
        y1 = 0
        x = 0

        for i in range(len(s)-1):
            x = 0  # Reset x to 0 at the beginning of each iteration
            if s[i] == r[0]:
                x += 1
            elif s[i] == r[1]:
                x += 5
            elif s[i] == r[2]:
                x += 10
            elif s[i] == r[3]:
                x += 50
            elif s[i] == r[4]:
                x += 100
            elif s[i] == r[5]:
                x += 500
            elif s[i] == r[6]:
                x += 1000
            
            if s[i] == 'I' and s[i+1] == 'V':
                x -= 2
            elif s[i] == 'I' and s[i+1] == 'X':
                x -= 2
            elif s[i] == 'X' and s[i+1] == 'L':
                x -= 20
            elif s[i] == 'X' and s[i+1] == 'C':
                x -= 20
            elif s[i] == 'C' and s[i+1] == 'D':
                x -= 200
            elif s[i] == 'C' and s[i+1] == 'M':
                x -= 200

            y1 += x
        
        if len(s) > 0:
            last_value = v[r.index(s[-1])]
            y1 += last_value
        
        return y1




                
        
                    
            

            


        