import math
import os
import random
import re
import sys
def countSwaps(a):
    n=len(a)
    numofswap=0
    for i in range(n-1) :
      for j in range (i,n):
          if a[i] > a[j] :
            a[i],a[j]=a[j],a[i]
            numofswap+=1
    print("Array is sorted in",numofswap,"swaps. ")
    print("First Element:", a[0])
    print("Last Element:", a[-1])
        
if __name__ == '__main__':
    
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))

    countSwaps(a)





