class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        l = 0
        # if len(arr) == 2:
        #     if arr[0] > arr[1]:
        #         arr[0],arr[1] = arr[1],arr[0]
            
        # else:
        while l < len(arr):
            if arr[l] - l != 0 and arr[l] < len(arr):
                arr[arr[l]],arr[l]= arr[l],arr[arr[l]]
            else:
                l += 1
        print(arr)
               
        for i in range(len(arr)):
            if arr[i] - i != 0:
               return i
        return len(arr)
             
        
             