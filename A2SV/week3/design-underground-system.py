class UndergroundSystem:
    def __init__(self):
        self.ci = {}  
        self.jt = {} 

    def checkIn(self, id: int, start: str, time: int) -> None:
        self.ci[id] = (start, time)

    def checkOut(self, id: int, end: str, time: int) -> None:
        start, start_time = self.ci[id]
        key = (start, end)  

        if key not in self.jt:
            self.jt[key] = []

        self.jt[key].append(time - start_time)
        del self.ci[id]

    def getAverageTime(self, start: str, end: str) -> float:
        key = (start, end)  
        times = self.jt[key]  
        return sum(times) / len(times)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)