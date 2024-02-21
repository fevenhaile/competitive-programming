class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:

        tasks.sort(key = lambda x : (x[1]-x[0]))
        ans = tasks[-1][1]
        now  = ans-tasks[-1][0]
        for i in range(len(tasks)-2,-1,-1):
            if now >=tasks[i][1]:
                now =now-tasks[i][0]
            else:
                ans += (tasks[i][1]-now)
                now = tasks[i][1]- tasks[i][0]
        return ans
        # tasks.sort(key = lambda x:x[1]-x[0])
        # plus = tasks[-1][1]
        # energy = plus - tasks[-1][0]
        # for i in range(len(tasks)-2,-1,-1):
        #     if energy >= tasks[i][1]:
        #         energy = energy - tasks[i][0]
        #     else:
        #         plus += (tasks[-1][1] - energy)
        #         energy += tasks[i][1] - tasks[i][0]
        # return plus
        