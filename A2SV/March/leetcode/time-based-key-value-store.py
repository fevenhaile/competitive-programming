class TimeMap:

    def __init__(self):
        self.dic = defaultdict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        self.dic[key].append([value,timestamp])
      
    def get(self, key: str, timestamp: int) -> str:
        # use a binary search
        res = ""
        val = self.dic.get(key,[])

        low = 0
        high = len(val) - 1

        while low <= high:
            mid =(low+high)//2
            if val[mid][1] > timestamp:
                high = mid - 1
            else:
                res = val[mid][0]
                low = mid + 1
               
        return res


        
        
        




        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)