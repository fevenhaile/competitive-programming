class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Here is a simple hint for binary search : if number of elements on 
        # right side is more than arr[mid] just go right side otherwise go on
        #  left side. 
        low = 0
        high = len(citations)-1
        res = 0
        while low <= high:
            mid = (low + high)//2
            if len(citations) - mid <= citations[mid]:
                res = len(citations) - mid
                high = mid - 1
            else:
                low = mid + 1
                
        return res
