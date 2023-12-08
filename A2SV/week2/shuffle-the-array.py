class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffearray = []
        for i in range(len(nums) - n):
            shuffearray.append(nums[i])
            shuffearray.append(nums[n])
            n +=1
        return shuffearray




        