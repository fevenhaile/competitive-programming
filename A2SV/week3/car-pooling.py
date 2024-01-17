from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timeline = [0] * 1001

        for trip in trips:
            passengers, start, end = trip
            timeline[start] += passengers
            timeline[end] -= passengers

        used_capacity = 0
        for passengers_change in timeline:
            used_capacity += passengers_change
            if used_capacity > capacity:
                return False

        return True