class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        totalsum=sum(arr)
        window=0
        
        for k in range(1,len(arr)+1,2):

            for i in range(len(arr) - k+1):
                window  += sum(arr[i:i+k])
                # print(i,sum(arr[i:i+k]))
        return window