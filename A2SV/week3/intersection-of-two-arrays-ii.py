class Solution(object):
    def intersect(self, nums1, nums2):
        result=[]
        for i in nums1:
            if(i in nums2):
                result.append(i)
                nums2.remove(i)
        return result        