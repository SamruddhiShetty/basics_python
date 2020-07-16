# basics_python

class Solution:
    def reverse(self, x: int) -> int:
        s=""
        while x!=0:
            s +=str(x%10)
            x = x//10
            
        return (int(s))
        
#this will exceed the time limit,hence not recommended

class Solution:
    def reverse(self, x: int) -> int:
        rev= int(str(abs(x))[: : -1])
        if rev.bit_length() < 32:
            if x<0:
                return (-rev)
            else:
                return rev
        else:
            return 0
 #this is solved using reversing string but can also solve using stack
