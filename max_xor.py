# basics_python
#find the maximum xor for the given string wherein the number of "set" should be less than 'k' value given

import math
import os
import random
import re
import sys

def maxXorValue(x, k):
    # Write your code here
    count=0
    y=''
    for i in range(len(x)):
        y=y+'1'
    r=''
    i=count=0
    while i<(len(x)) and count<k:
        if int(x[i]) ^ int(y[i])==1:
            count +=1
        r=r+str(int(x[i]) ^ int(y[i]))
        i +=1
    if i<len(x):
        while i<len(x):
            r=r+'0'
            i+=1
    return(r)    
                
            
                
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        k = int(input().strip())

        y = maxXorValue(s, k)

        fptr.write(y + '\n')

    fptr.close()
