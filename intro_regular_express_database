# basics_python
import re


if __name__ == '__main__':
    N = int(input())
    l=[]
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        x=re.search("@gmail.com",emailID)
        if x==None:
            pass
        else:
            l.append(firstName)
    l=sorted(l)
    for i in l:
        print(i)
