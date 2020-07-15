# basics_python

#using visit by row 
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        outlist=[""]*numRows
        k=0
        dummy=1
        for i in s:
            outlist[k] +=i
            k +=dummy
            if k==0 or k==numRows-1:
                dummy *=-1
        s1=""
        for i in outlist:
            s1 +=i
            
        return s1
 #efficiency is time=O(n) and space=O(n).
 
            
        
