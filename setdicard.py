n = int(input())
x = set(map(int, input().split()))
N=input()


x.pop()
x.remove(9)
x.discard(9)
x.discard(8)
x.remove(7)
x.pop()
x.discard(6)
x.remove(5)
x.pop()
x.discard(5)

print(sum(x))
    







