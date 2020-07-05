# basics_python

if __name__=="__main__":
    N, M= map(int, input().split())
    size=N-2
    size2=((M-2)//2)//3
    i=1
    space=size2
    while i<=size:
        print('-'*space*3+'.|.'*i+'-'*space*3)
        i=i+2
        space -=1
    size3=(M-7)//2
    print('-'*size3+'WELCOME'+'-'*size3)
    i=size
    space=1
    while i>=0:
        print('-'*space*3+'.|.'*i+'-'*space*3)
        i=i-2
        space +=1


# the above code is without the use of string alignment functions

#this code uses string alignment function

if __name__=="__main__":
    N, M= map(int, input().split())
    size=N-2
    i=1
    pattern='.|.'
    while i<=size:
        print((pattern*i).center(M,'-'))
        i=i+2
    print('WELCOME'.center(M,'-'))
    i=size
    while i>=0:
        print((pattern*i).center(M,'-'))
        i=i-2
