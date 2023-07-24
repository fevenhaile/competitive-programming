M=input()
ms=set(map(int,input().split()))
N=input()
ns=set(map(int,input().split()))

x=ms.symmetric_difference(ns)
z=sorted(x)


for i in z:
    print (i)



