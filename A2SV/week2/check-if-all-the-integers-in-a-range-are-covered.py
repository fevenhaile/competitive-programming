class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        Allranges = set(range(left, right + 1))
        Allranges2 = set()

        for range_values in ranges:
            start = range_values[0]
            end = range_values[1]
            Allranges2.update(range(start, end + 1))

        return Allranges.issubset(Allranges2)