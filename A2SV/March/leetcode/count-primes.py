class Solution:
    def countPrimes(self, n: int) -> int:
        # creat an array of len n with True
        if n < 2:
            return 0
        isprime = [True] *(n)
        isprime[0] =False
        isprime[1] =False
        for i in range(2,isqrt(n)+1):
            if isprime[i]:
                for j in range(i*i,n,i):
                    isprime[j] = False
        
        count = 0
        for i in range(len(isprime)):
            if isprime[i] == True:
                count+=1
        return count

        

        