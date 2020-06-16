# basics_python
def staircase(n):
    for i in range(n):
        print(' '*(n-(i+1)),end="")
        for j in range(n-(i+1),n):
            print('#',end="")
        print()

if __name__ == '__main__':
    n = int(input())

    staircase(n)
    
    
    
    output-
    6
    
     #
    ##
   ###
  ####
 #####
######
