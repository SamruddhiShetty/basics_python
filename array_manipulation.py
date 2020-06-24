# basics_python
import math
import os

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])
    max1=sum1=0
    l1=[0]*(n+1)      #including an extra element for calculation purpose
    for _ in range(m):
       a, b, k=  (int (n) for n in input().rstrip().split())
       l1[a-1]+=k
       if b<=len(l1):
        l1[b] -=k              #a logic used to support use of prefix algorithm to bring the efficiency to O(m+n) from O(mn).
    for i in range(n):
        sum1+=l1[i]           #"LOGIC" of prefix sum algorithm used
        max1=max(max1,sum1)


    fptr.write(str(max1) + '\n')

    fptr.close()
