from itertools import product
 
A=list(map(int,input().split()))
B=list(map(int,input().split()))


x=list(product(A,B))
for i in x:
    print(i,end=' ')
