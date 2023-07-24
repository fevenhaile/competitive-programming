M=input()
ms=set(map(int,input().split()))
N=input()
ns=set(map(int,input().split()))

x=ms.difference(ns)
y=ns.difference(ms)
z=sorted(x.union(y))


for i in z:
    print (i)



