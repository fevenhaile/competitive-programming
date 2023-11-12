class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude=[0]
        for i in range(len(gain)):
            altitude.append(gain[i]+altitude[-1])
            print(altitude)
        return max(altitude)