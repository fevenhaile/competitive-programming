class Solution(object):
    def dailyTemperatures(self, temperatures):
       st=[]
       ans=[0]*len(temperatures)

       for i in range (len(temperatures)):
           while st and temperatures[i]>temperatures[st[-1]]:
               idx=st.pop()
               ans[idx]=i-idx
           st.append(i)
       return ans
               