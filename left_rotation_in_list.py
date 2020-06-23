# basics_python
if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    a1=[]
    j=d
    for i in range(n):
        a1.append(a[j%n])
        j +=1
    print(" ".join(map(str,a1)))
      
            


eg:-
i/p:- 5 4
1 2 3 4 5

o/p:-
5 1 2 3 4
