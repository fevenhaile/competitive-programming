class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        mylist = [0]*len(boxes)
        
        for i in range(len(boxes)):
            total = 0
            for j in range(len(boxes)):
                if boxes[j] == "1":
                    mylist[i] += abs(i-j)
        return mylist
        