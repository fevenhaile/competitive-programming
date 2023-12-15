class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lessthan_pivot = []
        greaterthan_pivot = []
        equals = []
        result = []
        for i in range(len(nums)):
            if nums[i] < pivot:
                lessthan_pivot.append(nums[i])
            elif nums[i] > pivot:
                greaterthan_pivot.append(nums[i])
            else:
                equals.append(nums[i])

        print(lessthan_pivot)
        print(greaterthan_pivot)
        print(equals)
        return lessthan_pivot + equals + greaterthan_pivot
        


            
        


            

        