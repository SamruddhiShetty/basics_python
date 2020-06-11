# basics_python
def find_max(n,k):
    max1=0
    for i in range(1,n+1):   #this prevents repeated iteration over certain numbers 
        for j in range(1,i):
            x=i&j
            if max1<x<k:
                max1=x 
            if max1==k-1:
                return max1   #returning early saves time

    return max1






if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        print(find_max(n,k))


