class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n=len(nums)
        squares = 0
        for i in range(1,n+1):
            if n % i == 0:
                x=nums[i-1]**2
                squares += x
        print(squares)
        return squares