# basics_python
if __name__ == '__main__':
    N = int(input())
    l2=[]
    for i in range(N):
        command, *l1=input().strip().split()
        l1=list(map(int,l1))
        if command == 'insert':
            l2.insert(l1[0],l1[1])
        elif command=='print':
            print(l2)
        elif command=='remove':
            l2.remove(l1[0])
        elif command=='append':
            l2.append(l1[0])
        elif command=='sort':
            l2.sort()
        elif command=='pop':
            l2.pop()
        else:
            l2.reverse()
            
        
