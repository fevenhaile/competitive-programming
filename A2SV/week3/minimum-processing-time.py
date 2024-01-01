from typing import List

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        n = len(processorTime)  
         

        tasks.sort(reverse=True) 
        processorTime.sort()  

        min_time = 0  

        for i in range(n):
            for j in range(4):
                task_index = (i * 4) + j  
                processing_time = processorTime[i] + tasks[task_index]
                min_time = max(min_time, processing_time)

        return min_time





       

