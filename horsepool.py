# basics_python
def update_table(table, sub_string):
    for i in range(len(sub_string)):
        for j in table:
            if j==sub_string[i]:
                if (len(sub_string)-(i+1))==0:
                    pass
                else:
                    table[j]=len(sub_string)-(i+1) 
                break
    return(table)
    

def count_substring(string, sub_string):
    count=0
    size=len(sub_string)
    table={}
    for i in range(97, 123):
        table[chr(i)]=size
    for i in range(65, 91):
        table[chr(i)]=size
    table['#']=size
    table['_']=size
    table['@']=size
    table['$']=size
    table['&']=size
    table['*']=size
    table[' ']=size
    table['!']=size
    table[',']=size
    table['.']=size
    for i in range(11):
        table[str(i)]=size
    table=update_table(table, sub_string)
    i=size-1
    while i<=len(string)-1:
        k=0
        while k<=size-1 and sub_string[size-1-k]==string[i-k]:
            k +=1
        if k==size: 
            count +=1
            i +=1
        else:
            x=string[i]
            i=i+table[x]
    return(count)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
