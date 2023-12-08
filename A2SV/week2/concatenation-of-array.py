class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        duplicatearray = []
        for i in range(len(nums)):
            duplicatearray.append(nums[i])
        concatenated_array = nums + duplicatearray
        return concatenated_array

