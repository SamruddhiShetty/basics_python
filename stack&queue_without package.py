# basics_python
class Solution:
    def __init__(self):
        #i=0
        self.l1=[]
        self.l2=[]
    # Write your code here
    def pushCharacter(self,c1):
        self.l1.append(c1)
    def enqueueCharacter(self,c2):
        self.l2.append(c2)
    def popCharacter(self):
        return self.l1.pop()
    def dequeueCharacter(self):
        return self.l2.pop(0)


# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    
