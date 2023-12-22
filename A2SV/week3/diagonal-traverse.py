class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        myarray = []

        for row in range(len(mat)):
            for column in range(len(mat[0])):
                dic[row+column].append(mat[row][column])
        for key,value in dic.items():
            dic[key] = value
            if key % 2 == 0:
                myarray.append(value[::-1])
            else:
                myarray.append(value[::])
        print(dic)
        one_D_array = [j for i in myarray for j in i] 
        return one_D_array
        

      
                   

     

        