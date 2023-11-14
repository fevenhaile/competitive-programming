class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        counter = 0
        current_sum=sum(arr[:k-1])

        for i in range(len(arr)-k+1):
            current_sum += arr[i+k-1]
            if current_sum/k >= threshold:
                counter += 1
            current_sum -= arr[i] 
        return counter