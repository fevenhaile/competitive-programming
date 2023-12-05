class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        Capacity = capacity
        steps = 0

        for i in range(len(plants)):
            if plants[i] <= capacity:
                steps += 1
                capacity -= plants[i]
            else:
                steps += 2*i+1
                capacity = Capacity
                capacity -= plants[i]
        return steps