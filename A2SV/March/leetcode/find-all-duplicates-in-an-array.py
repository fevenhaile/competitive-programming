class Solution:
    def findDuplicates(self, arr: List[int]) -> List[int]:
        l = 0
        ans = []
        while l < len(arr):
            if arr[l] - l != 1 and arr[l] != arr[arr[l]-1]:
                arr[arr[l]-1],arr[l]= arr[l],arr[arr[l]-1]
            else:
                l += 1
        print(arr)
        for i in range(len(arr)):
            if arr[i] - i != 1:
                ans.append(arr[i])
        return ans
        