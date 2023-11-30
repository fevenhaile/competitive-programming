class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        total = sum(salary)
        return (total-salary[0]-salary[-1])/(len(salary)-2)
            
            

        
        