# basics_python
#USING EXPAND AROUND CENTRE

class Solution:
    def findPalindrome(self, s, left,  right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left -=1
            right +=1
        return s[left+1:right]
    
    def longestPalindrome(self, s: str) -> str:
        result=''
        if s=='' and s==None:
            return ''
        start=0
        final=0
        for i in range(len(s)):
            s1 =self.findPalindrome(s, i, i)
            s2 = self.findPalindrome(s, i, i+1)
            temp=s1 if len(s1)>len(s2) else s2
            result=temp if len(temp)>len(result) else result
        return result
#efficiency is O(n2) adnd space efficiency is O(n) 
