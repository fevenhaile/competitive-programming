class Solution(object):
    def majorityElement(self, nums):
        result,counter=0,0
        for i in nums:
            if counter==0:
                result=i
            counter+=(1 if i==result else -1)
        return result