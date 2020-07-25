# basics_python
#without converting it into string
#this method is done using half palindrome check method
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x%10==0 and x!=0) :
            return False
        a=x
        count= b=0
        while b<x:
            b=(b*10)+(x%10)
            x=x//10
            count +=1
        if x==b or x==b//10:
            return True
        else:
            return False
            
        
