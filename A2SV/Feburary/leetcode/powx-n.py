class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(z,y):
            if y == 0:
                return 1
            elif  y == 1:
                return z
            elif y < 0:
                return power(1/z,-y)
            elif y % 2 == 0:
                half = power(z,y//2)
                return half*half
            else:
                return z * power(z,y-1)
        return power (x,n)
            
       
            
            


        
        