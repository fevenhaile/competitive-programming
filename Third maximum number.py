class Solution(object):
    def thirdMax(self, nums):
        first = second = third = float('-inf')
        nums = set(nums)

        for num in nums:
            if num > first:
                third = second
                second = first
                first = num
            elif num > second and num != first:
                third = second
                second = num
            elif num > third and num != second and num != first:
                third = num

        if len(nums) < 3:
            return first  
        return third  

