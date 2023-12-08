class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mylist = []
        x = float('inf')

        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    if i + j < x:
                        x = i + j
                        mylist = [list1[i]]
                    elif i + j == x:
                        mylist.append(list1[i])

        return mylist