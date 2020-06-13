# basics_python
def mergesort(l):
    if len(l)<=1:
        return(l)
    else:
        m=len(l)//2
        a=mergesort(l[:m])
        b=mergesort(l[m:])
        return(merge(a,b))
    
    
def merge(a,b):
    c=[]
    i=0
    j=0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            c.append(a[i])
            i +=1
        else:
            c.append(b[j])
            j +=1
    while i<len(a):
        c.append(a[i])
        i +=1
    while j<len(b):
        c.append(b[j])
        j +=1
    return(c)
    
if __name__=="__main__":
    l=list(map(int,input().strip().split()))
    print(mergesort(l))
    
    
