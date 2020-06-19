# basics_python
def average(q):
    global student_record
    sum1=0
    sum1=sum(student_record[q])
    return(sum1/3)

if __name__=="__main__":
    N=int(input())
    student_record={}
    for _ in range(N):
        name, *line=input().strip().split()
        line=list(map(float,line))
        student_record[name]=line
    query=input()
    print("{0:.2f}".format(average(query)))
