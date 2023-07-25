N=int(input())
n=set(map(int,input().split()))
B=int(input())
b=set(map(int,input().split()))


x=n.union(b)
print(len(x))