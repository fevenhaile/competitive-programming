class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum(num for num in nums if num % 2 == 0)
        result = []

        for query in queries:
            val, index = query
            original_num = nums[index]

            nums[index] += val
            updated_num = nums[index]

            if original_num % 2 == 0:
                even_sum -= original_num

            if updated_num % 2 == 0:
                even_sum += updated_num

            result.append(even_sum)

        return result