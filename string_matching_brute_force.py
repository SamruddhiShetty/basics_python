# basics_python
def count_substring(string, sub_string):
    count=0
    m=len(sub_string)
    n=len(string)
    i=0
    while i<n-m+1:
        if string[i:i+m]==sub_string:
            count +=1
            i +=1
        else:
            i +=1
    return count



if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
