class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n == 1:
            return 5
        @cache
        def pow(x, y, mod):
            if y == 1:
                return x
            num = pow(x,y//2,mod)
            if y % 2 == 0:
                return (num * num) % mod
            return (num * num * x) % mod
        x = pow(5,n//2, (10**9)+7)
        y = pow(4,n//2, (10**9)+7)
        if n % 2 == 0:
            return  (x*y) % ((10**9)+7)
        else:
            return (x*y*5) % ((10**9)+7)
            
        