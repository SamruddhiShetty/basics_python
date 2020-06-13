# basics_python
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
swaps=0
for i in range(0,(len(a)-1)):
    for j in range(0,len(a)-1-i): #here the elements are being sorted at the end of the array,i.e from the last element
        if a[j]>a[j+1]:
            a[j], a[j+1]=a[j+1], a[j]
            swaps +=1

print("Array is sorted in {} swaps.".format(swaps))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[len(a)-1]))
