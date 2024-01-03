class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        list2 = []

        for i in range(len(points)):
            value = ((points[i][0])**2) + ((points[i][1])**2)
            list2.append((value,i))
        
        list2.sort()
        
        for i in range(k):
            result.append(points[list2[i][1]])
       
        return result
        
    


