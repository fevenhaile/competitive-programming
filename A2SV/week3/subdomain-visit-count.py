class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = defaultdict(int)
        answer = []
        for domain in cpdomains:
            count,value = domain.split()
            print(count,value)
            thedomains = value.split(".")
            for i in range(len(thedomains)):
                s = thedomains[i:]
                sliceddomains = ".".join(s)
                dic[sliceddomains] = int(count) + dic[sliceddomains]
        print(dic)
        for key,value in dic.items():
            answer.append(str(value)+ " "+ key)
        return answer





        


 
