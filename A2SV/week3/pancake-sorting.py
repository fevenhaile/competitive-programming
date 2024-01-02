class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        for i in range(len(arr) - 1, -1, -1):
            maxind = i
            for j in range(i, -1, -1):
                if arr[j] > arr[maxind]:
                    maxind = j
            if maxind != i:
                arr[:maxind+1] = arr[:maxind+1][::-1]
                result.append(maxind + 1)
                arr[:i+1] = arr[:i+1][::-1]
                result.append(i + 1)
        return result


