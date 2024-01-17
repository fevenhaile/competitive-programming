class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix = [0] * (n+2)
        for i in range(len(bookings)):
            prefix[bookings[i][0]] += bookings[i][2]
            prefix[(bookings[i][1])+1] -= bookings[i][2]
        x = 0
        result = []
        for i in range(1,n +1):
            x += prefix[i]
            result.append(x)
        return result
