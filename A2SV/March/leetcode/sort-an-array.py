class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(lefthalf,righthalf):
            l = 0
            r = 0
            result = []
            while l < len(lefthalf) and r < len(righthalf):
                if lefthalf[l] <= righthalf[r]:
                    result.append(lefthalf[l])
                    l += 1
                else:
                    result.append(righthalf[r])
                    r+=1
            result.extend(lefthalf[l:])
            result.extend(righthalf[r:])
            return result
        # merge sort functioin
        def mergesort(left,right,nums):
            # basecse
            if left == right:
                return [nums[right]]
            mid = (left+right)//2
            lefthalf = mergesort(left,mid,nums)
            righthalf = mergesort(mid+1,right,nums)

            return merge(lefthalf,righthalf)
        return mergesort(0,len(nums)-1,nums)