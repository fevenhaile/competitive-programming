class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        counter = 0
        window_sum = sum(arr[:k])
        for i in range(len(arr)-k+1):
            average = window_sum/k
            if average >= threshold:
                counter += 1
            window_sum-=arr[i]
            if i+k < len(arr):
                window_sum+=arr[k+i]

        return counter